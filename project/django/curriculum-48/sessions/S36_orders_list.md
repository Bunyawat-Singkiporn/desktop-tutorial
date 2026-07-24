# S36 — Orders list with join-style serializer fields

## Goal

List orders with readable related fields.

## Concept (5 min)

SerializerMethodField or source= for product_name, username, total

## Backend steps

- Order + OrderItem models
- List serializer with denormalized display fields

## Frontend steps

- Orders table page

## Check

- [ ] Orders show product names / totals
- [ ] Empty state ok

## Common bugs

- Exposing huge nested trees when a flat list is enough
