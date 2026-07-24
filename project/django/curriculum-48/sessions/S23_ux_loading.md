# S23 — UX: loading, empty, toast

## Goal

Polish Task Board UX states.

## Concept (5 min)

Loading spinner while fetching
Empty state when results=[]
Toast on success/error

## Backend steps

- No backend change required unless adding message fields

## Frontend steps

- isLoading / isEmpty flags
- Simple toast component
- Disable buttons while mutating

## Check

- [ ] Empty list does not look broken
- [ ] Success feedback on create

## Common bugs

- Infinite loading if fetch never settles — check errors
