# S16 — Error handling: 400 / 401 / 404 on UI

## Goal

Show user-friendly errors when the API fails.

## Concept (5 min)

Read response.ok; parse error JSON from DRF.
Map status to message: 400 validation, 401 login, 404 missing.

## Backend steps

- Force a 400 (empty title) and note response body shape

## Frontend steps

- Centralize apiFetch helper in src/api/client.js
- Show banner / toast on error
- Disable double-submit while loading

## Check

- [ ] Bad POST shows message, not silent fail
- [ ] Network error handled

## Common bugs

- Assuming error body is always a string
