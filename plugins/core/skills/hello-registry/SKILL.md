---
name: hello-registry
description: >-
  skill-registry가 이 머신에 제대로 설치·동기화되고 있는지 확인한다.
  사용자가 "레지스트리 확인", "registry 잘 깔렸어?", "hello registry" 등
  설치 상태 점검을 요청할 때 사용.
---

# hello-registry

skill-registry 설치 상태를 점검하고 결과를 보고하는 스킬입니다.

## 절차

1. 이 SKILL.md가 로드됐다는 사실 자체가 "마켓플레이스 → 로컬 캐시 → 스킬 로딩" 경로가
   동작한다는 증거입니다. 먼저 그 사실을 사용자에게 알리세요.
2. 아래를 확인해서 표로 보고하세요:
   - 이 스킬이 로드된 경로 (플러그인 캐시 아래인지)
   - `~/.claude/settings.json`에 `extraKnownMarketplaces.skill-registry`가 있고
     `autoUpdate`가 `true`인지 (false면 자동 동기화가 안 되므로 경고)
   - `enabledPlugins`에 `core@skill-registry`가 `true`인지
3. 문제가 발견되면 `bootstrap/install.sh`를 다시 실행하라고 안내하세요.

## 보고 형식

- 정상: "✅ skill-registry 정상 — 새 스킬은 merge 후 다음 세션에서 자동 반영됩니다."
- 비정상: 무엇이 빠졌는지와 복구 명령을 한 줄로.
