# S35 — Product create/edit form (FK id)

## Goal

Create and edit products including category id.

## Concept (5 min)

Write serializer accepts category as PK.
Read serializer may expose category_name.

## Backend steps

- Create/update product endpoints
- Validation: price >= 0, stock >= 0

## Frontend steps

- ProductForm page
- Edit mode loads detail then PATCH

## Check

- [ ] Create + edit work
- [ ] Validation errors shown

## Common bugs

- Sending nested category object by mistake
