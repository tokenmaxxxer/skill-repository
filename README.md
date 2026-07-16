# skill-registry

**스킬 단일 진실 원천(SSOT)**. 스킬을 여기에 merge하면, `git pull` 한 번으로
전 구성원의 Claude Code와 OpenCode에 반영됩니다.

## 동작 원리

```
[이 repo (SSOT)] ──(git pull)──▶ [각자 머신 ~/skill-registry/skills]
                                         │
                            ~/.claude/skills (symlink)
    ├──▶ Claude Code가 읽음
    └──▶ OpenCode가 읽음
```

- `~/.claude/skills`는 Claude Code와 OpenCode가 둘 다 기본 스킬 경로로 읽습니다.
- `install.sh`가 이 디렉터리를 `~/skill-registry/skills`로 심볼릭 링크합니다.
- 서버 없음. GitHub repo + 로컬 파일이 전부입니다.

## 설치 (1회)

```bash
git clone git@github.com:JiwonJung94/skill-repository.git ~/skill-registry
bash ~/skill-registry/install.sh
```

스킬을 추가할 때 어차피 이 repo가 필요하므로, 임시 디렉터리 대신 그대로 두고 씁니다.
나중에 업데이트하려면:

```bash
git -C ~/skill-registry pull
```

> 개인 repo라 `curl | bash`는 쓸 수 없습니다. SSH는 사내 repo 접근에 이미 쓰고 있어 추가 설정이 없습니다.

## 스킬 추가하기

1. `skills/<스킬명>/SKILL.md` 생성
   - frontmatter의 `name`은 디렉터리명과 일치, `description`은 "언제 이 스킬을 쓰는지"가
     드러나게 (자동 호출 판단 기준, 1024자 이하)
2. PR → merge되면 각자 `git -C ~/skill-registry pull`로 반영.

## 구조

```
skills/<스킬명>/SKILL.md           # 스킬 정의
install.sh                         # 1회 설정 스크립트
```

## 설계 원칙

- **main = 배포 채널.** merge가 곧 릴리스이다.
- **스킬은 이식 가능해야 한다.** 특정 repo 경로·시크릿에 의존하는 스킬은 받지 않는다.
- **도구 중립.** Claude Code와 OpenCode 양쪽에서 동작하는 것을 기본으로 한다.
