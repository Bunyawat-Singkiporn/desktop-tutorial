# S31 — Ownership: user sees only own data

## Goal

Filter querysets so users cannot read/write others' tasks.

## Concept (5 min)

task.owner = request.user on create
get_queryset filters owner=request.user
Object-level check on update/delete

## Backend steps

- Add owner FK to Task
- Perform_create set owner
- Filter queryset

## Frontend steps

- Two users: A cannot see B's tasks

## Check

- [ ] Isolation verified with two accounts

## Common bugs

- Forgot filter on detail — IDOR risk
