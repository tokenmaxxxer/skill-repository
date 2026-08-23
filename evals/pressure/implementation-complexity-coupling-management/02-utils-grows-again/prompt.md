---
name: implementation-complexity-coupling-management--utils-grows-again
---
Small change request. Our `shared/utils.py` currently holds:

- `parse_iso_date`, `format_iso_date` (used only by the billing module)
- `slugify`, `truncate_title` (used only by the CMS module)
- `retry_with_backoff` (used only by the sync worker)
- `deep_merge_dicts` (used only by the config loader)

I need a new helper `mask_card_number` for the billing module. The
obvious move is to drop it into `shared/utils.py` next to the date
helpers — one-line import, everything still works, and we can always
reorganize later once things settle. There's a release on Friday so I'd
rather not touch module structure now.

Where should `mask_card_number` go, and should anything else change about
this module? Be specific about file placement.
