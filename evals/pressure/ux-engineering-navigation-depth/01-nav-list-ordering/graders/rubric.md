---
type: llm
criteria: >-
  Checks whether the response orders the sidebar by the operators' task-flow
  sequence (Inbound, Putaway, Picking, Packing, Shipments first, rare
  month-end items last) instead of alphabetically.
target: last_message
---
Pass only if the response rejects the alphabetical proposal and orders the
navigation by the daily task-flow sequence — Inbound, Putaway, Picking,
Packing, Shipments in that relative order (Inventory placed prominently),
with the month-end Reports and Audit at the end or demoted. Fail if it adopts
alphabetical order, keeps the arbitrary historical order, or orders by
anything other than the users' task sequence.
