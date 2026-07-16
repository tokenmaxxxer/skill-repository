# skill-registry

**스킬 단일 진실 원천(SSOT)**. 스킬을 여기에 merge하면, 별도 배포 절차 없이
전 구성원의 Claude Code(CLI·VSCode·데스크톱)에 자동으로 반영됩니다.

## 동작 원리

```
[이 repo (SSOT)] ──(세션 시작 시 autoUpdate가 자동 pull)──▶ [각자 머신 ~/.claude/plugins 캐시]
                                                                └▶ Claude Code가 스킬을 읽는 기본 경로
```

- 이 repo는 Claude Code **플러그인 마켓플레이스**입니다 ([.claude-plugin/marketplace.json](.claude-plugin/marketplace.json)).
- 각 구성원은 아래 부트스트랩을 **머신당 1회**만 실행합니다. 이후에는 Claude Code가
  세션 시작 시 백그라운드로 이 repo를 확인하고 변경분을 캐시에 반영합니다
  (`autoUpdate: true`). 수동 업데이트 명령이 필요 없습니다.
- **`/plugin install`만으로는 안 되는 이유**: 제3자 마켓플레이스는 `autoUpdate`
  기본값이 **false**입니다 ([문서][au]). CLI/UI로 설치하면 등록과 설치는 되지만
  자동 반영이 꺼진 채로 남고, 경고도 없습니다. `autoUpdate: true`를 선언적으로
  기록하는 것이 부트스트랩 스크립트의 핵심 역할입니다 — 이 줄을 지우지 마세요.

[au]: https://code.claude.com/docs/en/discover-plugins
- 서버 없음. GitHub repo + 로컬 파일이 전부입니다.

## 설치 (1회)

```bash
git clone git@github.com:JiwonJung94/skill-repository.git ~/skill-registry
bash ~/skill-registry/bootstrap/install.sh
```

스킬을 추가할 때 어차피 이 repo가 필요하므로, 임시 디렉터리 대신 그대로 두고 씁니다.
나중에 다시 돌리려면 `git -C ~/skill-registry pull` 후 같은 스크립트를 실행하면 됩니다
(멱등).

> private repo라 `curl | bash`는 쓸 수 없습니다 — raw.githubusercontent.com이 404를
> 반환하는데 `curl -f`는 빈 출력으로 끝나서, `bash`가 **아무 일도 안 하고 성공**한
> 것처럼 보입니다. SSH는 사내 repo 접근에 이미 쓰고 있어 추가 설정이 없습니다.

마켓플레이스와 플러그인 활성화 항목을 `~/.claude/settings.json`에 병합하고
(기존 설정 보존, 멱등, 실행 전 자동 백업), 플러그인을 설치합니다. 확인은 새 세션에서:

> "레지스트리 확인해줘" → `hello-registry` 스킬이 응답하면 정상.

## 스킬 추가하기

1. 플러그인 아래에 디렉터리 생성: `plugins/<플러그인>/skills/<스킬명>/SKILL.md`
   - frontmatter의 `name`은 디렉터리명과 일치, `description`은 "언제 이 스킬을 쓰는지"가
     드러나게 (Claude의 자동 호출 판단 기준, 1536자 이하)
2. **`version`을 올립니다 — 이게 배포 트리거입니다.**
   올릴 곳은 [plugin.json](plugins/core/.claude-plugin/plugin.json) **한 곳뿐**입니다.
   스킬 추가는 기능 추가이므로 MINOR(`0.1.0` → `0.2.0`), 오타·문구 수정은 PATCH.
   - **왜 필요한가**: Claude Code는 해석된 version이 사용자가 이미 가진 것과 같으면
     "이미 최신"으로 보고 캐시를 갱신하지 않습니다 (강제 `claude plugin update`도
     `already at the latest version`으로 거부). 즉 **version을 안 올리면 merge돼도
     아무에게도 배포되지 않고**, autoUpdate도 정상 동작하므로 아무도 알아채지 못합니다.
   - **왜 한 곳인가**: version 해석 순서는 plugin.json → marketplace.json의 `plugins[]`
     항목 → git 커밋 SHA이고, plugin.json에 version이 있으면 그 값이 **항상 조용히
     이깁니다**. 그래서 marketplace 항목에 version을 같이 두면 그 값은 무시되면서 실제
     배포되는 version을 가리는 거짓 기록이 됩니다 — [공식 문서][ver]가 두 곳에 두지
     말라고 명시적으로 경고합니다. `marketplace.json`의 `metadata.version`은 마켓플레이스
     자신의 매니페스트 버전이라 플러그인 배포와 무관합니다(올려도 아무 일도 안 일어납니다).
   - 깜빡해도 CI가 막아주지만(`validate.py --base`), 이유를 알고 올리는 편이 낫습니다.

[ver]: https://code.claude.com/docs/en/plugin-marketplaces
3. 새 플러그인을 만들 경우: `plugins/<이름>/.claude-plugin/plugin.json` 작성 후
   [marketplace.json](.claude-plugin/marketplace.json)의 `plugins[]`에
   `"source": "./plugins/<이름>"` 항목 추가 (맨 앞 `./` 필수)
   - **주의**: `autoUpdate`는 이미 설치된 플러그인만 갱신합니다. 기존 플러그인에
     스킬을 추가하면 전원 자동 반영되지만, **플러그인 자체를 새로 추가**하면 기존
     구성원에게 자동 활성화되지 않습니다 — 기본 배포에 넣으려면
     [bootstrap/install.sh](bootstrap/install.sh)의 `PLUGINS` 배열에 추가하고
     재실행을 공지하세요 (개별로는 `/plugin install <이름>@skill-registry`).
4. 로컬 검증: `python3 scripts/validate.py`
   (version 범프까지 확인하려면 `python3 scripts/validate.py --base origin/main`)
5. PR → CI(validate)가 게이트 → merge되면 배포 완료. 각자 다음 세션부터 반영.

## 구조

```
.claude-plugin/marketplace.json   # 카탈로그 — 여기 등록돼야 배포됨
plugins/
  core/                           # 공통 플러그인 (팀별 플러그인은 형제로 추가: sales, frontend, ...)
    .claude-plugin/plugin.json
    skills/<스킬명>/SKILL.md
bootstrap/install.sh              # 구성원 1회 설정 스크립트
scripts/validate.py               # 구조 검증기 (CI와 동일)
.github/workflows/validate.yml    # merge 게이트 — PR마다 위 검증기 실행 (+ version 범프 검사)
```

## 설계 원칙

- **main = 배포 채널.** merge가 곧 릴리스이므로 CI 통과 없이 merge하지 않는다.
- **플러그인 = 구독/업데이트 단위.** 팀별 스킬은 팀별 플러그인으로 분리해
  필요한 팀 것만 켤 수 있게 한다 (`enabledPlugins`).
- **스킬은 이식 가능해야 한다.** 특정 repo 경로·시크릿에 의존하는 스킬은 받지 않는다.
