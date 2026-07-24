# S15 — Edit / Delete from the table

## Goal

Toggle done with PATCH and remove with DELETE from the UI.

## Concept (5 min)

Each row action calls a different method on the same resource URL.

## Backend steps

- PATCH and DELETE verified in API client

## Frontend steps

- Toggle done checkbox -> PATCH
- Delete button -> DELETE + confirm
- Update local state or refetch

## Check

- [ ] Toggle and delete work end-to-end

## Common bugs

- Updating wrong id
- UI state out of sync with server
