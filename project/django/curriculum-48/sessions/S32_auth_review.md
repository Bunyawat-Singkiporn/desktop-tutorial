# S32 — Auth review: lock Task CRUD behind auth

## Goal

Integrate Auth project with Task Board and demo.

## Concept (5 min)

Register -> Login -> Me -> owned Tasks only

## Backend steps

- Permissions consistent across endpoints
- Seed two users for demo

## Frontend steps

- Full flow demo
- Navbar shows user + logout

## Check

- [ ] Anonymous cannot CRUD
- [ ] Ownership holds

## Common bugs

- Leaving AllowAny on write endpoints
