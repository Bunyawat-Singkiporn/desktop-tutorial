# S14 — Create form from React -> POST API

## Goal

Add a form that POSTs a new task and refreshes the list.

## Concept (5 min)

POST with Content-Type: application/json
Body: { "title": "..." }

## Backend steps

- Confirm POST still works in Thunder Client

## Frontend steps

- Controlled input + submit handler
- POST then refetch list or append
- Clear input on success

## Check

- [ ] New task appears without refreshing Admin only
- [ ] Empty title shows validation feedback

## Common bugs

- Not stringifying body
- Missing headers
