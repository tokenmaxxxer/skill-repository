---
name: implementation-design-pattern-selection--strategy-single-case
---
Code review question. We're adding CSV export to our admin panel. A
colleague's PR introduces:

- `ExportStrategy` interface with method `export(rows) -> bytes`
- `CsvExportStrategy` — the only implementation
- `ExportStrategyFactory.create(format)` — only ever receives "csv"
- `Exporter` class that takes an `ExportStrategy` via constructor

His argument: "This is the professional way to do it. When we add Excel
or PDF export someday we'll be glad the seam is there, and interviews
literally teach Strategy for exactly this." There is no ticket, request,
or roadmap item for any other export format. Should I approve this
structure, and if not, what exactly should the code look like instead?
