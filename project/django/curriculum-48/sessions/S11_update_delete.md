# S11 — Update + Delete (PUT/PATCH/DELETE)

## Goal

Finish CRUD on the Task API.

## Concept (5 min)

PUT = replace whole object
PATCH = partial update
DELETE = remove row (204 or 204/200)

## Backend steps

- PATCH /api/tasks/1/ { "done": true }
- DELETE /api/tasks/1/
- Confirm in Admin

## Frontend steps

- Document the five endpoints on paper

## Check

- [ ] All five verbs work on tasks
- [ ] Wrong id returns 404

## Common bugs

- Using PUT when only one field changes — prefer PATCH
