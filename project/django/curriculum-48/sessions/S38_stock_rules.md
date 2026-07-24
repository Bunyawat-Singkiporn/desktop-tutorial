# S38 — Stock update API + business rules

## Goal

Decrease stock when ordering; reject overselling.

## Concept (5 min)

Business rules live in serializer/view/service — not only in the UI.

## Backend steps

- On order create: check stock, decrement
- 400 if qty > stock

## Frontend steps

- Show error when stock insufficient
- Refresh product stock on products page

## Check

- [ ] Stock decreases correctly
- [ ] Oversell blocked

## Common bugs

- Race conditions — mention select_for_update for advanced
