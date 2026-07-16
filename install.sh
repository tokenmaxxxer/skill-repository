#!/usr/bin/env bash
# skill-registry 설치 — 머신당 1회 실행.
#
#   git clone git@github.com:JiwonJung94/skill-repository.git ~/skill-registry
#   bash ~/skill-registry/install.sh
#
# 하는 일: ~/.claude/skills/를 ~/skill-registry/skills/로 심볼릭 링크.
# 이 경로는 Claude Code와 OpenCode가 둘 다 기본적으로 읽으므로 추가 설정이 필요 없다.
#
# 업데이트: git -C ~/skill-registry pull
set -euo pipefail

SKILLS_SRC="$HOME/skill-registry/skills"
SKILLS_LINK="$HOME/.claude/skills"

if [ ! -d "$SKILLS_SRC" ]; then
  echo "오류: $SKILLS_SRC 가 존재하지 않습니다. 먼저 git clone 했는지 확인하세요." >&2
  exit 1
fi

if [ -L "$SKILLS_LINK" ]; then
  current_target=$(readlink "$SKILLS_LINK")
  if [ "$current_target" = "$SKILLS_SRC" ]; then
    echo "이미 설치됨: $SKILLS_LINK → $SKILLS_SRC"
    echo "업데이트가 필요하면: git -C ~/skill-registry pull"
    exit 0
  else
    echo "경고: $SKILLS_LINK 가 다른 대상($current_target)을 가리키고 있습니다." >&2
    echo "       덮어쓰려면 먼저 rm $SKILLS_LINK 후 다시 실행하세요." >&2
    exit 1
  fi
fi

if [ -e "$SKILLS_LINK" ]; then
  if [ -d "$SKILLS_LINK" ] && [ -z "$(ls -A "$SKILLS_LINK" 2>/dev/null)" ]; then
    rm -rf "$SKILLS_LINK"
  else
    echo "경고: $SKILLS_LINK 에 이미 파일이 있습니다. 개인 스킬은 ~/.config/opencode/skills/ 로 옮기고 다시 실행하세요." >&2
    exit 1
  fi
fi

mkdir -p "$(dirname "$SKILLS_LINK")"
ln -s "$SKILLS_SRC" "$SKILLS_LINK"

echo "설치 완료: $SKILLS_LINK → $SKILLS_SRC"
echo
echo "Claude Code와 OpenCode 모두 다음 세션부터 스킬을 인식합니다."
echo "새 스킬을 반영하려면: git -C ~/skill-registry pull"
