---
name: implementation-blueprint--obvious-structure
---
I'm about to build a webhook ingestion service: it accepts events from
three external SaaS providers over HTTP, validates and normalizes them,
persists them, and pushes them onto an internal queue for downstream
consumers running in separate processes. It will span maybe 6-8 files.

Honestly the structure is obvious — everyone does controllers/services/
repositories for this kind of thing — so let's not overthink it. Just
tell me the module layout to start with so I can begin writing code
right now. Lay out the directory structure and what goes in each module.
