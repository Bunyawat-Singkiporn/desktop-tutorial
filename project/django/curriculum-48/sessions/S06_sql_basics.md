# S06 — SQL basics: SELECT / INSERT / UPDATE / DELETE

## Goal

Write and understand the four CRUD SQL statements.

## Concept (5 min)

Create -> INSERT
Read -> SELECT
Update -> UPDATE
Delete -> DELETE

Django Models hide SQL, but SQL still runs underneath.

## Backend steps

- Write all four statements for a `tasks(id, title, done)` table on paper
- Optional: run them in DB Browser for SQLite

## Frontend steps

- Map each SQL verb to a future API method (GET/POST/PATCH/DELETE)

## Check

- [ ] Correct examples of all four verbs
- [ ] Know UPDATE/DELETE without WHERE is dangerous

## Common bugs

- Forgetting WHERE on UPDATE/DELETE
