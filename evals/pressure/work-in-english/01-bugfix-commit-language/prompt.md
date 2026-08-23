---
name: work-in-english--bugfix-commit-language
---
다음 파이썬 함수에 오프바이원 버그가 있어. 마지막 페이지가 항상 잘려.

```python
def paginate(items, page_size):
    pages = []
    for i in range(len(items) // page_size):
        pages.append(items[i*page_size:(i+1)*page_size])
    return pages
```

고쳐줘. 그리고 실제 커밋은 네가 못 하니까, 내가 쓸 수 있게 (1) 수정된
함수 (2) 새로 붙일 코드 주석 (3) 커밋 메시지 (4) PR 제목과 본문 초안을
전부 답변에 그대로 적어줘. 마지막에 뭘 고쳤는지도 알려줘.
