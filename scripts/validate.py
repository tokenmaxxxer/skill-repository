#!/usr/bin/env python3
"""skill-registry 구조 검증기 — merge 게이트(CI)와 로컬 점검 공용.

검사 항목:
  1. marketplace.json이 유효하고, 모든 plugins[] 항목의 source가 "./"로 시작하며
     실제 디렉터리와 plugin.json이 존재하고 이름이 일치한다.
  2. 각 플러그인의 skills/*/SKILL.md frontmatter에 name/description이 있고,
     name은 디렉터리명과 일치하며, description은 1536자 이하이다.
  3. 마켓플레이스에 등록되지 않은 plugins/ 하위 디렉터리가 없다 (등록 누락 방지).
  4. version이 plugin.json에만 있다 (marketplace.json plugins[] 항목에는 없다).
  5. (--base <ref> 지정 시) 플러그인 내용이 바뀌었다면 version도 올랐다.

    4·5번이 핵심이다. Claude Code의 version 해석 순서는 plugin.json →
    marketplace.json의 plugins[] 항목 → git 커밋 SHA이고, plugin.json에 version이
    있으면 그 값이 항상 이긴다. 그래서 version은 plugin.json 한 곳에만 둔다 —
    marketplace 항목에 같이 두면 plugin.json이 조용히 이기면서 그 값은 무시되므로,
    어긋난 순간 실제 배포되는 version을 가리는 거짓 기록이 된다. 공식 문서가
    두 곳에 두는 것을 명시적으로 경고한다.
      https://code.claude.com/docs/en/plugin-marketplaces
    그리고 해석된 version이 사용자가 이미 가진 것과 같으면 "이미 최신"으로 보고
    캐시를 갱신하지 않는다 (강제 `claude plugin update`조차 "already at the latest
    version"으로 거부). 즉 version을 올리지 않으면 스킬을 merge해도 아무에게도
    배포되지 않으며, autoUpdate도 정상 동작하므로 누구도 알아채지 못한다.
    사람의 기억에 맡기지 않고 여기서 막는다.

    marketplace.json의 metadata.version은 마켓플레이스 자신의 매니페스트 버전이라
    플러그인 배포와 무관하다. 검사하지 않는다.

사용법:
    python3 scripts/validate.py                  # 구조만 검사 (로컬)
    python3 scripts/validate.py --base origin/main   # + version 범프 검사 (CI)

의존성 없음(Python 3.9+ stdlib). 실패 시 exit 1, 사유를 전부 출력.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_DESC = 1536
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        err(f"{path}: frontmatter(---)가 없음")
        return {}
    # 무의존 미니 파서: 최상위 "key: value"와 ">-/|" 멀티라인만 지원
    fm: dict[str, str] = {}
    key = None
    for line in m.group(1).splitlines():
        top = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if top:
            key, val = top.group(1), top.group(2).strip()
            fm[key] = "" if val in (">-", ">", "|", "|-") else val
        elif key and line.startswith((" ", "\t")):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm


def check_skill(skill_dir: Path) -> None:
    md = skill_dir / "SKILL.md"
    if not md.exists():
        err(f"{skill_dir}: SKILL.md 없음")
        return
    fm = parse_frontmatter(md)
    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        err(f"{md}: frontmatter에 name 없음")
    elif name != skill_dir.name:
        err(f"{md}: name '{name}' ≠ 디렉터리명 '{skill_dir.name}'")
    if not desc:
        err(f"{md}: frontmatter에 description 없음 (자동 호출 판단 기준이라 필수)")
    elif len(desc) > MAX_DESC:
        err(f"{md}: description {len(desc)}자 > {MAX_DESC}자 (초과분은 잘림)")


def check_plugin(plugin_dir: Path, entry: dict) -> None:
    registered_name = entry["name"]
    manifest = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        err(f"{plugin_dir}: .claude-plugin/plugin.json 없음")
        return
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"{manifest}: JSON 파싱 실패 — {e}")
        return
    if data.get("name") != registered_name:
        err(f"{manifest}: name '{data.get('name')}' ≠ marketplace 등록명 '{registered_name}'")
    # version은 plugin.json 한 곳에만. 해석 순서상 plugin.json이 항상 이기므로,
    # marketplace 항목의 version은 무시되면서 실제 배포 version을 가리기만 한다.
    mkt_ver, plugin_ver = entry.get("version"), data.get("version")
    if not plugin_ver:
        err(f"{manifest}: version 없음 (version이 배포 트리거다)")
    if mkt_ver is not None:
        err(
            f"marketplace.json[{registered_name}]: version '{mkt_ver}'가 있다 — "
            f"version은 plugin.json에만 둘 것. plugin.json이 항상 이기므로 이 값은 "
            f"무시되면서 실제 배포되는 version을 가린다"
        )
    skills_root = plugin_dir / "skills"
    if skills_root.is_dir():
        for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
            check_skill(skill_dir)


def git(*args: str) -> str | None:
    """git 명령 실행. 실패하면 None (검사를 건너뛰기 위함)."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), *args],
            capture_output=True, text=True, check=True,
        )
        return out.stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def check_version_bump(base: str, registered: dict) -> None:
    """플러그인 내용이 바뀌었는데 version이 그대로면 배포되지 않는다 — 막는다."""
    changed = git("diff", "--name-only", f"{base}...HEAD")
    if changed is None:
        err(
            f"--base {base} 로 diff를 못 냈다. CI라면 actions/checkout에 "
            f"fetch-depth: 0 이 필요하다 (얕은 clone은 base ref가 없다)."
        )
        return

    files = [f for f in changed.splitlines() if f.strip()]
    for name, source in sorted(registered.items()):
        prefix = source.lstrip("./").rstrip("/") + "/"
        touched = [f for f in files if f.startswith(prefix)]
        # plugin.json만 바뀐 경우는 버전만 올린 릴리스 커밋일 수 있으므로 제외
        content = [f for f in touched if not f.endswith(".claude-plugin/plugin.json")]
        if not content:
            continue

        manifest = f"{prefix}.claude-plugin/plugin.json"
        old_raw = git("show", f"{base}:{manifest}")
        if old_raw is None:
            continue  # 새로 추가된 플러그인 — 비교 대상 없음
        try:
            old_ver = json.loads(old_raw).get("version")
        except json.JSONDecodeError:
            continue
        new_ver = json.loads((ROOT / manifest).read_text(encoding="utf-8")).get("version")

        if old_ver == new_ver:
            shown = "\n      ".join(content[:5])
            more = f"\n      … 외 {len(content) - 5}건" if len(content) > 5 else ""
            err(
                f"plugins/{name}: 내용이 바뀌었는데 version이 '{old_ver}' 그대로다.\n"
                f"      → 올리지 않으면 merge돼도 아무에게도 배포되지 않는다.\n"
                f"      → {manifest} 의 version을 올릴 것 (marketplace.json이 아니다).\n"
                f"      변경된 파일:\n      {shown}{more}"
            )


def main() -> int:
    ap = argparse.ArgumentParser(description="skill-registry 구조 검증기")
    ap.add_argument(
        "--base", metavar="REF",
        help="이 ref와 비교해 version 범프 여부까지 검사 (CI용, 예: origin/main)",
    )
    args = ap.parse_args()

    mkt_path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        mkt = json.loads(mkt_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"FAIL {mkt_path}: {e}")
        return 1

    registered: dict[str, str] = {}
    for entry in mkt.get("plugins", []):
        name, source = entry.get("name", ""), entry.get("source", "")
        if not name:
            err(f"marketplace.json: name 없는 plugins[] 항목 {entry}")
            continue
        if not source.startswith("./"):
            err(f"marketplace.json[{name}]: source는 './'로 시작해야 함 (현재 '{source}')")
            continue
        plugin_dir = ROOT / source
        if not plugin_dir.is_dir():
            err(f"marketplace.json[{name}]: 디렉터리 없음 — {source}")
            continue
        registered[name] = source
        check_plugin(plugin_dir, entry)

    plugins_root = ROOT / "plugins"
    if plugins_root.is_dir():
        for d in sorted(p for p in plugins_root.iterdir() if p.is_dir()):
            if d.name not in registered:
                err(f"plugins/{d.name}: marketplace.json에 등록되지 않음")

    if args.base:
        check_version_bump(args.base, registered)

    if errors:
        print(f"FAIL — {len(errors)}건:")
        for e in errors:
            print(f"  - {e}")
        return 1
    skill_count = sum(1 for _ in ROOT.glob("plugins/*/skills/*/SKILL.md"))
    scope = " (+ version 범프)" if args.base else ""
    print(f"OK — 플러그인 {len(registered)}개, 스킬 {skill_count}개 검증 통과{scope}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
