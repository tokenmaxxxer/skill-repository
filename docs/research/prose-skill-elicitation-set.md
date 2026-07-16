# Elicitation set — prose-skill A/B pre-registration, Field 1

**Status: FROZEN on commit. Date stamp: 2026-07-16.**

This file is the frozen elicitation set referenced in
`docs/research/prose-skill-ab-preregistration.md`, Field 1 and Field 2. It is
committed **before the skill's rule text exists**. Per the pre-registration:

- This file must not be edited after the base-rate pilot (OFF-arm, n=20 on
  Stratum A) has been run and committed. Any change after that point voids
  the pilot's Gate-1 denominators.
- No prompt below was written with knowledge of any rule's wording, because
  no rule wording exists yet.
- A revision to this set is a new elicitation set under a new pre-registration
  — it may not be scored against data already collected with this version.

No prompt in this document contains style guidance. None instructs how to
write (no "clearly," "concisely," "avoid bullets," "use a table"). Where a
prompt asks for enumerable content (CLI flags, error codes) or for a
definition before an analogy, that is the substance of the request a real
user would send, not a style instruction layered on top of it — see the
per-item rationale in Stratum B.

---

## Amendment 1 (2026-07-16)

The amendment window is open only because the base-rate pilot (Field 2 of
the pre-registration: OFF-arm, n=20 on Stratum A) has not yet run — no
Gate-1 denominators exist yet to void. Two additions, both appended without
renumbering or editing any existing id (A01–A20, B01–B42, C01–C10
unchanged):

1. **Stratum B, Pattern 8 — 아첨 (B43–B54).** Field 1 reserved Stratum B
   slots for translationese patterns, to be filled "after the research
   round" once that research existed. It has since returned: 3 of 7 seed
   translationese patterns occur zero times across 116,754 characters of
   AI-generated Korean — near-absent, not merely rare. Those reserved slots
   are vacant and are reallocated here to a pattern with a stronger
   evidence grade (sycophancy: 검증된 사실 at both symptom and cause level)
   that the existing set already elicits by accident.
2. **Stratum E — certainty gradient within one document (E01–E06).** New
   stratum; adapts three existing prompts' topics rather than inventing new
   ones. Carries its own honest-limit note (below its heading).

---

## Stratum A — neutral explanatory prompts

20 prompts (10 Korean, 10 English), carrying H1 and H3. Spread across five
document-genre axes (4 prompts each, 2 Korean + 2 English), with reader
background varied per prompt the way a real requester would convey it —
inside the ask, not as a style directive.

| ID | Lang | Document type | Reader background | Prompt |
|---|---|---|---|---|
| A01 | KO | Tutorial | Novice | 저는 프로그래밍을 처음 배우는 사람이고 지금까지 파이썬 print문 정도만 써봤습니다. 명령줄에서 git을 써서 처음으로 코드를 커밋하고 원격 저장소에 푸시하는 과정을 처음부터 따라 할 수 있게 설명해 주세요. |
| A02 | EN | Tutorial | Expert | I've used Git for years but have never set up a rebase workflow with interactive rebase and autosquash. Walk me through doing an interactive rebase with fixup commits on a real feature branch. |
| A03 | KO | How-to | Intermediate | PostgreSQL 테이블에 이미 데이터가 100만 건 있는 상태에서 다운타임 없이 NOT NULL 컬럼을 추가하려면 어떻게 해야 하나요? |
| A04 | EN | How-to | Novice | I just deployed my first website and someone told me I need HTTPS. I don't know anything about certificates. How do I actually get HTTPS working on a domain I bought last week? |
| A05 | KO | Reference | Expert | 우리 팀 내부 위키에 올릴 자료로, Kubernetes에서 Pod가 가질 수 있는 재시작 정책(restartPolicy) 값들과 각각이 어떤 컨트롤러(Job, Deployment, DaemonSet 등)와 함께 쓰일 수 있는지 정리해줘. 이미 쿠버네티스를 운영해본 사람들이 볼 자료야. |
| A06 | EN | Reference | Intermediate | Our team already knows the basics of REST APIs. Write reference documentation for the pagination parameters our internal search API accepts, for other engineers who'll be integrating with it. |
| A07 | KO | Explanation/conceptual | Novice | CPU와 GPU가 왜 다른 종류의 계산에 특화되어 있는지, 컴퓨터를 잘 모르는 사람도 이해할 수 있게 설명해줘. |
| A08 | EN | Explanation/conceptual | Expert | For an audience of backend engineers who already understand ACID, explain why serializable isolation in Postgres can still produce different results than true serial execution. |
| A09 | KO | Design/decision writeup | Intermediate | 우리 팀이 마이크로서비스 간 통신 방식으로 REST 대신 gRPC를 채택하기로 했어요. 왜 이 결정을 내렸는지, 어떤 대안을 검토했는지 팀 위키에 남길 결정 문서를 작성해줘. |
| A10 | EN | Design/decision writeup | Expert | We're a team that's already run Kafka in production for two years. Write up the decision record for why we chose to migrate our event bus from Kafka to a managed alternative, including what we're giving up. |
| A11 | KO | Tutorial | Intermediate | AWS Lambda는 몇 번 써봤지만 아직 로컬에서 SAM CLI로 디버깅해 본 적은 없어. VS Code에서 브레이크포인트를 걸고 Lambda 함수를 로컬 디버깅하는 방법을 처음부터 알려줘. |
| A12 | EN | Tutorial | Novice | I've never written a single line of SQL before. Teach me how to write a query that pulls rows from one table based on a value in another table, starting from nothing. |
| A13 | KO | How-to | Novice | 리액트가 뭔지도 잘 모르는데, 회사에서 만들라고 한 간단한 To-Do 리스트 앱에 로컬 스토리지 저장 기능을 추가해야 합니다. 어떻게 해야 하나요? |
| A14 | EN | How-to | Expert | Our service already runs behind an nginx reverse proxy with mTLS between internal services. How do I rotate the internal CA certificate without causing a service outage? |
| A15 | KO | Reference | Novice | 리눅스를 이제 막 쓰기 시작한 사람인데, ls 명령어에 붙일 수 있는 옵션들이 각각 뭘 하는지 정리해서 알려줘. |
| A16 | EN | Reference | Intermediate | Document the exit codes our internal CLI tool returns, for engineers who already use the tool day to day but keep asking what each code means. |
| A17 | KO | Explanation/conceptual | Expert | 이미 TCP 3-way handshake는 알고 있는 사람에게, TCP의 혼잡 제어(congestion control)가 왜 필요한지 설명해줘. |
| A18 | EN | Explanation/conceptual | Novice | My friend asked me why my phone's battery drains faster in cold weather and I couldn't answer. Can you explain what's actually happening inside the battery, assuming I don't know any chemistry? |
| A19 | KO | Design/decision writeup | Novice | 저희는 이제 막 3명이서 스타트업을 시작했고 아직 데이터베이스를 하나도 안 정해봤어요. 왜 MySQL 대신 PostgreSQL을 쓰기로 했는지, 나중에 팀원이 늘었을 때 볼 수 있게 문서로 남겨줘. |
| A20 | EN | Design/decision writeup | Intermediate | Our small team has shipped a couple of internal tools with plain JSON config files. Write the decision doc for why we're switching to a schema-validated config format, for teammates who'll inherit this later. |

---

## Stratum B — licit-use prompts

Carries H2. The harm screen: for each of the 7 banned patterns, ≥5 prompts
engineered so the pattern's surface form is the *correct* output. 6 prompts
per pattern below (42 total, 21 Korean / 21 English), each with the exact
proposition its correct instance must carry — this is what the extractor
checks, not the surface string.

### Pattern 1 — 부정대비 ("단순히 X가 아니라 Y다")

Licit when X is a real, widespread misconception the reader actually holds.

**B01** (KO) — Docker vs. VM
Prompt: 많은 사람들이 도커 컨테이너를 '가벼운 가상머신' 같은 거라고 생각하던데, 실제로 컨테이너가 가상머신과 어떻게 다른지 설명해줘.
Required proposition: Docker containers are not virtual machines; they share the host OS kernel (no separate guest kernel or hardware-level hypervisor virtualization), which is why they start faster and carry less overhead than VMs.

**B02** (EN) — HTTPS padlock and trust
Prompt: A lot of non-technical users think the padlock icon in the browser means a website is safe to enter their password on. Is that actually true?
Required proposition: The padlock only certifies that the connection to that domain is encrypted (and that a certificate was issued to that domain name); it does not certify that the site's operator is trustworthy or that the site isn't phishing/malicious.

**B03** (KO) — Garbage collection and memory leaks
Prompt: 자바는 가비지 컬렉터가 있으니까 메모리 누수 걱정을 안 해도 된다고 하는 사람들이 있던데, 정말 그런가요?
Required proposition: Garbage collection reclaims memory that is no longer reachable, but it cannot reclaim memory still reachable via a reference the program no longer needs (e.g., objects held in a static collection, unclosed listeners); memory leaks remain possible in a garbage-collected language.

**B04** (EN) — VPN anonymity
Prompt: I keep seeing ads claiming a VPN makes you completely anonymous online. Is that accurate?
Required proposition: A VPN hides your IP address from the destination server and your ISP's view of traffic content/destination, but it does not make you anonymous — the VPN provider can see your traffic, and sites can still identify or track you via cookies, browser fingerprinting, or account logins.

**B05** (KO) — Force push and commit loss
Prompt: git push --force를 쓰면 예전 커밋들이 완전히 사라져서 아무도 복구할 수 없다고 들었는데 맞나요?
Required proposition: A force push moves the remote branch pointer, but the previous commits are not immediately destroyed — they remain reachable via the reflog on any machine that had them, and via any other branch or tag still pointing to them, until garbage-collected; "gone forever" is not accurate for a force push alone.

**B06** (EN) — "Schemaless" NoSQL
Prompt: Our new hire keeps saying we don't need to plan a schema because we're using MongoDB and it's "schemaless." Is that a fair way to think about it?
Required proposition: MongoDB documents don't require a schema to be declared to the database engine, but the application still reads and writes data with an implicit, consistent shape — "schemaless" means schema enforcement moved to the application layer, not that no schema exists.

### Pattern 2 — 예고 문장 ("조건은 셋이다")

Licit when the announced count genuinely informs — it inverts an expectation or answers a count the reader explicitly asked for.

**B07** (KO) — Postgres isolation levels vs. SQL standard
Prompt: PostgreSQL 문서를 보면 트랜잭션 격리 수준이 SQL 표준에는 네 단계로 정의되어 있다고 하는데, PostgreSQL이 실제로 내부적으로 구현하는 격리 수준은 몇 가지인가요?
Required proposition: PostgreSQL implements only 3 distinct isolation levels internally (Read Committed, Repeatable Read, Serializable), even though the SQL standard defines 4 (including Read Uncommitted), because Postgres's MVCC makes Read Uncommitted behave identically to Read Committed.

**B08** (EN) — CAP theorem
Prompt: In a distributed database, can you actually get consistency, availability, and partition tolerance all at the same time?
Required proposition: No — when a network partition occurs, the system can preserve at most 2 of the 3 properties (consistency+partition tolerance, or availability+partition tolerance); it cannot preserve all 3 simultaneously during a partition.

**B09** (KO) — Idempotent HTTP methods
Prompt: 재시도 로직을 안전하게 짜려면 멱등성이 있는 HTTP 메서드에만 자동 재시도를 걸어야 한다고 들었어요. HTTP에서 멱등성이 보장되는 메서드가 정확히 몇 개이고 뭔가요?
Required proposition: Exactly 5 of the commonly used HTTP methods are defined as idempotent — GET, PUT, DELETE, HEAD, and OPTIONS (POST and PATCH are not idempotent by spec).

**B10** (EN) — Git object types
Prompt: Under the hood, git stores everything as objects in the .git/objects directory. How many distinct types of objects does git actually use?
Required proposition: Git uses exactly 4 object types — blob, tree, commit, and tag.

**B11** (KO) — SOLID principle count
Prompt: 객체지향 설계 원칙으로 SOLID라는 말을 많이 쓰는데, 이게 정확히 몇 개의 원칙을 묶어서 부르는 말인가요?
Required proposition: SOLID is an acronym for exactly 5 principles — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.

**B12** (EN) — TLS 1.3 vs 1.2 handshake round trips
Prompt: How many round trips does a full TLS 1.3 handshake need compared to TLS 1.2, and why does that matter for page load time?
Required proposition: TLS 1.3 reduces the full handshake to exactly 1 round trip, down from 2 round trips in TLS 1.2, and supports 0-RTT resumption for repeat connections.

### Pattern 3 — 메타공지 ("이 문서는 ~를 다룬다")

Licit in a long document where the reader needs a scope statement to know whether to keep reading. Each prompt below asks for one document that must cover several named areas, so a reader arriving for only one of them is a real scenario.

**B13** (KO) — Backend onboarding doc
Prompt: 새로 입사한 백엔드 개발자가 처음부터 끝까지 읽고 우리 시스템 전체 아키텍처, 로컬 개발 환경 세팅, 배포 프로세스, 장애 대응 절차까지 다 알 수 있는 긴 온보딩 문서를 하나 써줘.
Required proposition: States, before the first section, that the document covers all four named areas (architecture, local dev setup, deployment, incident response), so a reader who only needs one can tell whether to keep reading.

**B14** (EN) — Billing service reference
Prompt: Write a complete reference for engineers who'll maintain our internal billing service: I need it to cover the data model, the API contract, retry/idempotency semantics, and the reconciliation job all in one document.
Required proposition: States up front, before the first topic, that the document covers all four named areas — data model, API contract, retry/idempotency semantics, reconciliation job.

**B15** (KO) — Coding convention doc
Prompt: 우리 프로젝트의 코딩 컨벤션을 이번 기회에 아예 하나의 긴 문서로 정리하고 싶어요. 네이밍 규칙, 커밋 메시지 규칙, 브랜치 전략, 코드 리뷰 기준까지 전부 담아서 써줘.
Required proposition: States near the top that the single document covers all four named areas — naming, commit messages, branching, code review.

**B16** (EN) — Auth service design doc
Prompt: I need a single long design document for our new authentication service that walks through the threat model, the token format, the rotation strategy, and the migration plan from the old system, all together, since different teams will each only care about one section.
Required proposition: States, before the sections begin, which of the four named topics the document covers, since the prompt itself signals that different readers each care about only one.

**B17** (KO) — Incident runbook
Prompt: 장애 대응 런북을 하나 만들려고 하는데, 배포 실패, DB 커넥션 풀 고갈, 캐시 서버 다운, 트래픽 급증 이렇게 네 가지 장애 유형에 대한 대응 절차를 한 문서에 다 넣어줘.
Required proposition: States up front which of the four named incident types the runbook covers, so an on-call engineer under time pressure can jump to the right section instead of reading serially.

**B18** (EN) — Data engineer onboarding doc
Prompt: Write one long onboarding doc for new data engineers that covers how our data warehouse is structured, how the ETL pipelines are scheduled, our naming conventions for tables, and how to request access to production data — all as a single reference they'll come back to repeatedly.
Required proposition: States at the start which of the four named topics the document covers, since the prompt frames it as a repeatedly-referenced document rather than a one-pass read.

### Pattern 4 — 과장 선언 / 최상급

Licit when a mechanism actually backs the superlative — the answer must name the mechanism, not just repeat the claim.

**B19** (KO) — Rust memory safety
Prompt: 왜 러스트(Rust)가 메모리 안전성 면에서 C++보다 우수하다고들 하나요? 실제로 어떤 차이가 있는 건가요?
Required proposition: States the mechanism — Rust's ownership/borrow-checker system enforces memory safety (no use-after-free, no data races on shared mutable state) at compile time without a garbage collector, which C++ has no compiler-enforced equivalent of.

**B20** (EN) — Binary search "fastest"
Prompt: Is it true that binary search is the fastest way to find an item in a sorted array, and why?
Required proposition: States the mechanism — binary search's O(log n) comparisons vs. linear search's O(n), and that no comparison-based algorithm can beat O(log n) on an already-sorted array (an asymptotic lower-bound argument) — not a bare assertion of superiority.

**B21** (KO) — HTTP/2 speed claim
Prompt: HTTP/2가 HTTP/1.1보다 훨씬 빠르다고 하는데 정확히 어떤 메커니즘 때문에 그런 거예요?
Required proposition: States the mechanism — HTTP/2 multiplexes multiple requests over a single TCP connection, eliminating application-layer head-of-line blocking and the extra handshakes multiple HTTP/1.1 connections require.

**B22** (EN) — Bloom filter space efficiency
Prompt: I heard that a Bloom filter is the most space-efficient way to check whether an element is probably in a set. What makes that true?
Required proposition: States the mechanism — trading a bounded, tunable false-positive rate for sub-linear space via k hash functions over a bit array, instead of storing the elements (or their full hashes) themselves.

**B23** (KO) — AES security claim
Prompt: AES가 지금까지 알려진 대칭키 암호화 알고리즘 중에서 사실상 가장 안전하다고 하는 이유가 뭔가요?
Required proposition: States the grounding — no practical (better-than-brute-force) cryptanalytic attack is publicly known against full-round AES despite decades of open cryptanalysis, and its key space makes brute force computationally infeasible.

**B24** (EN) — Hash table average-case lookup
Prompt: Why do people say a hash table gives you the fastest average-case lookup of any general-purpose data structure?
Required proposition: States the mechanism — with a good hash function and low load factor, a hash table computes a direct array index from the key (O(1) expected), avoiding the comparison-based traversal that gives trees O(log n) and lists O(n); the claim is scoped to average case and general-purpose use.

### Pattern 5 — 불릿·표·개조식

Licit when the content is a list by nature: CLI flags, config keys, error codes, comparison matrices. No prompt below names the output format — the list-shape comes from the content being asked for.

**B25** (KO) — curl flags
Prompt: curl 명령어에서 자주 쓰는 옵션들 좀 정리해줘. -X, -H, -d, -o 이런 것들이 뭘 하는지.
Required proposition: Presents each flag (-X, -H, -d, -o, etc.) as a discrete entry mapping flag to function, since the content is an enumerable set of independent CLI flags.

**B26** (EN) — Deploy script exit codes
Prompt: What are all the exit codes our internal deploy script can return, and what does each one mean?
Required proposition: Presents each exit code as a discrete entry (code to meaning), since exit codes are a discrete enumerable mapping, not a narrative.

**B27** (KO) — API error codes
Prompt: 우리 API가 반환하는 에러 코드들이 뭐가 있고 각각 어떤 상황에서 발생하는지 알려줘. 400, 401, 403, 404, 429, 500대 코드 다 포함해서.
Required proposition: Maps each named error code (400, 401, 403, 404, 429, 5xx) to its triggering condition as discrete entries, since error codes are a fixed finite set with no natural prose connective between them.

**B28** (EN) — Database comparison matrix
Prompt: Compare Postgres, MySQL, and SQLite across licensing, whether they support JSON columns, and whether they support full-text search out of the box.
Required proposition: Presents the three databases against the three named criteria as a grid where each cell is independently checkable, since a multi-item-by-multi-criterion comparison is inherently tabular content.

**B29** (KO) — Deployment environment variables
Prompt: 우리가 쓰는 쿠버네티스 클러스터에 배포할 때 필요한 환경변수 목록이 있는데, DATABASE_URL, REDIS_URL, JWT_SECRET, LOG_LEVEL, PORT 이렇게 5개 각각이 뭘 하는지랑 필수인지 선택인지 알려줘.
Required proposition: Maps each of the 5 named environment variables to its purpose and required/optional status as discrete entries, since this is a fixed enumerable configuration set.

**B30** (EN) — Stripped proxy headers
Prompt: List every HTTP request header our internal proxy strips before forwarding to the backend — Authorization, Cookie, X-Forwarded-For, and Host — and why each one gets stripped.
Required proposition: Maps each of the 4 named headers to its stripping rationale as discrete entries, since this is a fixed enumerable set of independent facts.

### Pattern 6 — 비유

Licit as support *after* an operational definition is established. Required propositions check both content (the definition) and order (definition before analogy).

**B31** (KO) — Pointers
Prompt: 포인터가 정확히 뭔지, 그리고 왜 초보자들이 어려워하는지 설명해줘. 나는 C를 배운 지 일주일 됐어.
Required proposition: States an operational definition of a pointer (a variable whose stored value is a memory address, used to indirectly access/modify the value at that address) before any analogy appears.

**B32** (EN) — Closures
Prompt: What is a closure in JavaScript, actually? I keep seeing people just say it's like a backpack a function carries around, but I don't get what's really happening.
Required proposition: States an operational definition of a closure (a function bundled with references to the variables from its enclosing lexical scope, which remain accessible after the outer function returns) before any analogy is introduced.

**B33** (KO) — Recursion
Prompt: 재귀함수가 뭔지 도무지 이해가 안 돼요. 함수가 자기 자신을 부른다는 게 무슨 뜻인지부터 제대로 알고 싶어요.
Required proposition: States the operational definition of recursion (a function that calls itself with a modified/smaller input, combined with a base case that stops the calls) before any supporting analogy.

**B34** (EN) — Race conditions
Prompt: Explain what a race condition actually is, mechanically — not just "two things happening at once," I want to understand what's really going wrong in the code.
Required proposition: States an operational definition (correctness depends on the relative timing/interleaving of two or more threads/processes accessing shared state, and an unintended interleaving produces an incorrect result) before any analogy.

**B35** (KO) — Thread vs. process
Prompt: 쓰레드(thread)와 프로세스(process)가 정확히 뭐가 다른 건지 설명해줘. 나중에 비유를 들어줘도 좋지만 먼저 진짜 정의부터 알고 싶어.
Required proposition: States the operational definitions (a process = independent memory space + OS-scheduled unit of resource allocation; a thread = a unit of execution within a process sharing that process's memory) before any analogy, per the reader's explicit request.

**B36** (EN) — Hash functions
Prompt: Can you explain what a hash function is, technically? Feel free to use an analogy if it helps, but I want to actually understand the properties first.
Required proposition: States the operational definition/properties of a hash function (deterministic mapping from arbitrary-size input to fixed-size output, plus the properties relevant to the stated context) before any analogy.

### Pattern 7 — 번호 교차참조 ("3장에서 본 X")

Licit in a genuinely long, numbered document. Each prompt establishes a multi-chapter/section document where the requested section depends on content already placed in an earlier numbered section.

**B37** (KO) — 5-chapter architecture doc, ch. 4 references ch. 2
Prompt: 우리 팀 신입 온보딩용으로 총 5장짜리 시스템 아키텍처 문서를 쓰고 있는데, 지금 4장인 '배포 파이프라인'을 쓰는 중이야. 2장에서 설명한 서비스 간 통신 방식을 다시 언급해야 하는 부분이 있는데, 그 부분을 포함해서 4장을 써줘.
Required proposition: Includes a cross-reference naming chapter 2 by number when the inter-service communication method comes up, rather than re-explaining it from scratch or referencing it without the chapter number.

**B38** (EN) — 6-chapter pipeline guide, ch. 5 references ch. 3
Prompt: I'm writing a 6-chapter internal guide to our data pipeline. I'm now on chapter 5, "Monitoring and Alerting," and I need to refer back to the retry logic I already fully explained in chapter 3 rather than re-explaining it. Write chapter 5.
Required proposition: Includes a numbered cross-reference to chapter 3 (e.g., "as described in Chapter 3") when retry logic comes up, since the prompt explicitly forbids re-explaining it.

**B39** (KO) — 8-section API guideline, sec. 7 references sec. 3
Prompt: 지금 사내 API 설계 가이드라인 문서를 8개 섹션으로 나눠서 쓰고 있어요. 7번 섹션 '에러 처리'를 쓰는 중인데, 3번 섹션에서 정의한 표준 에러 응답 포맷을 그대로 재사용해야 해요. 7번 섹션 내용을 써줘.
Required proposition: Cross-references section 3 by number instead of redefining the error response format inline or omitting the reference.

**B40** (EN) — Numbered runbook, sec. 9 references sec. 6
Prompt: This is part of a long, numbered runbook — I'm drafting section 9, "Rollback Procedure." It needs to assume the reader already went through the pre-rollback checks in section 6, and just point back there instead of repeating them. Write section 9.
Required proposition: Includes a numbered reference to section 6 (e.g., "complete the checks in Section 6") rather than restating its content, since the prompt explicitly instructs pointing back instead of repeating.

**B41** (KO) — 10-chapter K8s guide, ch. 9 references ch. 5
Prompt: 총 10장짜리 쿠버네티스 운영 가이드를 쓰고 있어요. 지금 9장 '트러블슈팅'을 쓰는 중인데, 5장에서 다룬 리소스 제한(resource limits) 설정이 원인이 되는 장애 케이스가 있어서 그 내용을 참조해야 해요. 9장을 써줘.
Required proposition: Cross-references chapter 5 by number rather than re-deriving the resource-limit content or leaving the causal connection unstated.

**B42** (EN) — 8-chapter architecture handbook, ch. 7 references ch. 4
Prompt: I'm writing chapter 7 of an 8-chapter architecture handbook, titled "Disaster Recovery." The recovery procedure depends entirely on the backup strategy from chapter 4, so it has to reference that chapter directly instead of restating it. Write chapter 7.
Required proposition: Includes a numbered cross-reference to chapter 4 rather than restating the backup strategy or leaving the dependency implicit.

---

## Stratum C — depth-demanding prompts

10 prompts (5 Korean, 5 English). Each correct answer must descend to a
named mechanism and name a failure condition (when the thing breaks or the
rule stops holding). Depth is demanded through the substance of the
question, not through a style instruction. Mechanism and failure condition
are recorded as ground truth for later extraction.

**C01** (KO) — Optimistic vs. pessimistic locking
Prompt: read/write 락(lock) 대신 optimistic locking(낙관적 락)을 쓰면 왜 성능이 좋아지는지, 그리고 낙관적 락이 오히려 손해인 상황은 언제인지 알려줘.
Mechanism: optimistic locking avoids holding a lock during the read-modify-write window, instead checking a version/timestamp at commit time, so readers never block writers and vice versa.
Failure condition: worse than pessimistic locking under high write contention on the same rows — most transactions fail the version check and retry, wasting completed work and causing thrashing/livelock.

**C02** (EN) — Index cost on writes
Prompt: Why does adding an index to a database column sometimes make write performance worse, and under what circumstances does that actually start to matter in practice?
Mechanism: every insert/update/delete on an indexed column must also update the index's data structure (e.g., B-tree rebalancing), adding I/O and CPU per write.
Failure condition: becomes a real practical problem specifically on write-heavy tables carrying many indexes (or large/high-cardinality indexed columns), where cumulative index-maintenance cost exceeds the read-side benefit.

**C03** (KO) — TCP reliability guarantee
Prompt: TCP가 신뢰성 있는 전송을 보장한다고 하는데, 정확히 어떤 메커니즘으로 그렇게 하는 건가요? 그리고 그 보장이 실제로 깨지는 경우가 있나요?
Mechanism: sequence numbers, acknowledgments, retransmission on timeout/duplicate-ACK, and checksums.
Failure condition: the guarantee is scoped to the connection, not end-to-end application correctness — it breaks when the connection is reset/torn down mid-transfer (e.g., a peer crashes after sending but before the ACK is processed), leaving the sender unable to know whether the last write was actually received.

**C04** (EN) — Bloom filter false positives
Prompt: How does a Bloom filter avoid false negatives while still using so little memory, and when can it actually give you a wrong answer?
Mechanism: insertion sets k bits via k hash functions and never clears them, so a queried element that was actually inserted always has all its bits set — no false negatives by construction.
Failure condition: produces false positives when other inserted elements' hash collisions happen to set all k bits for a never-inserted element; the rate rises as the ratio of inserted elements to bit-array size (load factor) grows past the filter's designed capacity.

**C05** (KO) — CDN latency
Prompt: CDN이 웹사이트를 빠르게 만들어준다고 하는데, 어떤 원리로 그런 거고, CDN을 붙여도 오히려 느려지거나 별 효과가 없는 경우는 언제인가요?
Mechanism: caches static content at edge servers geographically closer to the requesting user, cutting round-trip latency and offloading the origin.
Failure condition: little or no benefit (or added overhead) for highly dynamic, per-user, uncacheable content; when origin and most users are already geographically close; or on a cold cache miss where the edge still fetches from origin, adding a hop instead of saving one.

**C06** (EN) — Stale DNS caching
Prompt: Explain how DNS caching actually speeds things up, and describe a situation where stale DNS caching becomes a real operational problem.
Mechanism: resolvers cache a domain's IP mapping for its TTL, serving repeated lookups locally instead of querying the authoritative server.
Failure condition: becomes an operational problem when the underlying IP changes before the cached TTL expires — e.g., during failover/migration, clients or intermediate resolvers keep sending traffic to a decommissioned or reassigned IP until the stale record naturally expires.

**C07** (KO) — React useEffect dependency array
Prompt: 리액트에서 useEffect의 의존성 배열(dependency array)이 정확히 어떤 원리로 재실행 여부를 결정하는지, 그리고 이것 때문에 실제로 버그가 생기는 대표적인 상황을 알려줘.
Mechanism: React re-runs the effect when any value in the dependency array is not referentially/value-equal (Object.is) to its previous-render value; it does not track values used in the effect body but omitted from the array.
Failure condition: the classic stale-closure bug — a value used inside the effect but omitted from the dependency array keeps closing over the value from the render in which the effect was first created, using outdated data until something forces the array to include it.

**C08** (EN) — Round robin load balancing
Prompt: Why does load balancing with round robin sometimes fail to actually distribute load evenly across servers in practice?
Mechanism: round robin assigns requests to backends in a fixed rotating order regardless of each server's current load, capacity, or the cost of the individual request.
Failure condition: fails to balance evenly when requests have unequal processing cost, backends have unequal capacity, or connections are long-lived (WebSocket/keep-alive) — round robin only balances at connection-assignment time and cannot rebalance already-open long-lived connections as load shifts.

**C09** (KO) — LRU cache eviction
Prompt: 메모리 캐시에 LRU(Least Recently Used) 정책을 쓰면 왜 효과적인지, 그리고 LRU가 오히려 캐시 적중률을 떨어뜨리는 접근 패턴이 있는지 알려줘.
Mechanism: evicts the least-recently-accessed item on the theory that recently used items are likelier to be reused soon (temporal locality).
Failure condition: performs badly on a sequential scan larger than the cache (e.g., a full table scan touching every item once) — every access is a miss that evicts an item that would otherwise be reused soon, while the one-time scan items push out items with real reuse value.

**C10** (EN) — Exponential backoff and retry storms
Prompt: How does exponential backoff with retries actually reduce the risk of overloading a struggling service, and is there a scenario where retries with backoff make an outage worse instead of better?
Mechanism: increases wait time between successive retries (typically doubling, often with jitter), spreading retry traffic over time and reducing the instantaneous request rate versus immediate/fixed-interval retries.
Failure condition: a retry-storm/thundering-herd scenario — a large number of clients failing and backing off at roughly the same time can synchronize into correlated bursts that re-overload the recovering service, especially with absent or insufficient jitter, potentially preventing full recovery.

---

## Counts

| Stratum | Korean | English | Total |
|---|---|---|---|
| A — neutral explanatory | 10 | 10 | 20 |
| B — licit-use (7 patterns × 6) | 21 | 21 | 42 |
| C — depth-demanding | 5 | 5 | 10 |
| **All strata** | **36** | **36** | **72** |

Stratum B per-pattern breakdown (all patterns at 6, minimum required was 5):

| Pattern | IDs | Count |
|---|---|---|
| 1 — 부정대비 | B01–B06 | 6 |
| 2 — 예고 문장 | B07–B12 | 6 |
| 3 — 메타공지 | B13–B18 | 6 |
| 4 — 과장 선언/최상급 | B19–B24 | 6 |
| 5 — 불릿·표·개조식 | B25–B30 | 6 |
| 6 — 비유 | B31–B36 | 6 |
| 7 — 번호 교차참조 | B37–B42 | 6 |

No deviation from the requested counts: Stratum A hit 20 (10/10) exactly,
Stratum C hit 10 (5/5) exactly, Stratum B exceeded the ≥5-per-pattern floor
uniformly (6 per pattern) with distinct topics per prompt — no near-duplicates
padding the count.
