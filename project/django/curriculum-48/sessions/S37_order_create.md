# S37 — Order create flow + line items

## Goal

Create an order with one or more line items in one API call.

## Concept (5 min)

Writable nested serializer or explicit service in create()
Use transaction.atomic()

## Backend steps

- POST /api/orders/ with items: [{product_id, qty}]
- atomic create Order + OrderItems

## Frontend steps

- Create Order page: pick products + qty
- Redirect to orders list on success

## Check

- [ ] Order + items appear together
- [ ] Failure rolls back (no half order)

## Common bugs

- Creating items without transaction
