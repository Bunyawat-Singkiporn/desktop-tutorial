# S21 — Categories FK + dropdown from second API

## Goal

Assign each task a category from a separate list endpoint.

## Concept (5 min)

FK in JSON is often just category: <id>
UI loads /api/categories/ for a select dropdown.

## Backend steps

- Category model; Task.category FK
- Category list API
- Accept category id on Task write

## Frontend steps

- Load categories into <select>
- Show category name on table (serializer field category_name)

## Check

- [ ] Create task with category works
- [ ] Null category handled

## Common bugs

- Sending category name instead of id
