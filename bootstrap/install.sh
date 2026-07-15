#!/usr/bin/env bash
# skill-registry 부트스트랩 — 머신당 1회 실행.
#
#   git clone git@github.com:JiwonJung94/skill-repository.git ~/skill-registry
#   bash ~/skill-registry/bootstrap/install.sh
#
# private repo이므로 raw.githubusercontent.com은 404다 (curl | bash는 빈 입력을
# 받아 조용히 exit 0 하므로 절대 쓰지 말 것).
#
# 하는 일:
#   1. ~/.claude/settings.json에 마켓플레이스(autoUpdate 포함)와 플러그인 활성화
#      항목을 병합한다. 기존 설정은 보존하며 멱등이다.
#   2. claude CLI로 플러그인을 설치한다. settings.json만으로는 설치되지 않으므로
#      (enabledPlugins는 활성화 플래그일 뿐) 이 단계가 필수다.
# 설치 후에는 Claude Code가 세션 시작 시 알아서 원격 repo와 동기화한다.
set -euo pipefail

MARKETPLACE_NAME="skill-registry"
GITHUB_REPO="JiwonJung94/skill-repository"
PLUGINS=("core")   # 새 플러그인을 기본 배포에 넣으려면 여기에 추가

python3 - "$MARKETPLACE_NAME" "$GITHUB_REPO" "${PLUGINS[@]}" <<'PY'
import json, sys
from pathlib import Path

marketplace, repo, *plugins = sys.argv[1:]
path = Path.home() / ".claude" / "settings.json"
path.parent.mkdir(parents=True, exist_ok=True)

settings = {}
if path.exists():
    text = path.read_text(encoding="utf-8").strip()
    if text:
        try:
            settings = json.loads(text)
        except json.JSONDecodeError as e:
            sys.exit(f"오류: {path} 가 올바른 JSON이 아닙니다({e}). 수동으로 고친 뒤 다시 실행하세요.")
    backup = path.with_suffix(".json.bak")
    backup.write_text(text, encoding="utf-8")
    print(f"기존 설정 백업: {backup}")

mkts = settings.setdefault("extraKnownMarketplaces", {})
mkts[marketplace] = {
    "source": {"source": "github", "repo": repo},
    "autoUpdate": True,
}
enabled = settings.setdefault("enabledPlugins", {})
for p in plugins:
    enabled[f"{p}@{marketplace}"] = True

path.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"완료: {path}")
print(f"  마켓플레이스   {marketplace} → github:{repo} (autoUpdate: true)")
for p in plugins:
    print(f"  플러그인 활성화 {p}@{marketplace}")
PY

# settings.json의 extraKnownMarketplaces만으로 마켓플레이스 clone은 자동으로 되지만,
# enabledPlugins는 "설치된 플러그인을 켜라"는 플래그일 뿐 설치를 유발하지 않는다.
# 즉 아래 install 단계가 플러그인을 실제로 받아오는 유일한 경로다 — 실패하면 치명적.
find_claude() {
  if command -v claude >/dev/null 2>&1; then command -v claude; return 0; fi
  # VS Code 확장에 번들된 CLI (PATH에 없는 것이 기본).
  # 로컬은 ~/.vscode, Remote-SSH/WSL 서버는 ~/.vscode-server에 확장이 깔린다.
  local ext_root bundled
  for ext_root in "$HOME/.vscode" "$HOME/.vscode-server" "$HOME/.cursor-server"; do
    bundled=$(ls -d "$ext_root"/extensions/anthropic.claude-code-*/resources/native-binary/claude \
              2>/dev/null | sort -V | tail -1)
    if [ -n "$bundled" ] && [ -x "$bundled" ]; then echo "$bundled"; return 0; fi
  done
  for c in "$HOME/.claude/local/claude" "/usr/local/bin/claude" "/opt/homebrew/bin/claude"; do
    if [ -x "$c" ]; then echo "$c"; return 0; fi
  done
  return 1
}

if CLAUDE=$(find_claude); then
  echo "claude CLI: $CLAUDE — 플러그인을 설치합니다."
  "$CLAUDE" plugin marketplace add "$GITHUB_REPO" 2>/dev/null || true
  failed=()
  for p in "${PLUGINS[@]}"; do
    "$CLAUDE" plugin install "${p}@${MARKETPLACE_NAME}" || failed+=("$p")
  done
  if [ ${#failed[@]} -gt 0 ]; then
    echo
    echo "실패: ${failed[*]} — 위 오류를 확인하세요." >&2
    exit 1
  fi
  echo
  echo "끝. Claude Code 새 세션에서 \"레지스트리 확인해줘\"라고 말해 hello-registry 스킬이 뜨는지 확인하세요."
else
  # 여기서 조용히 끝내면 아무것도 설치되지 않은 채 "완료"로 보인다. 반드시 알린다.
  echo >&2
  echo "경고: claude CLI를 찾지 못해 플러그인을 설치하지 못했습니다." >&2
  echo "      설정은 기록됐지만 스킬은 아직 사용할 수 없습니다." >&2
  echo >&2
  echo "      Claude Code 세션에서 아래를 실행해 마무리하세요:" >&2
  for p in "${PLUGINS[@]}"; do
    echo "        /plugin install ${p}@${MARKETPLACE_NAME}" >&2
  done
  exit 1
fi
