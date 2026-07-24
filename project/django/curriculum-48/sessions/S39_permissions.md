# S39 — Admin vs API roles (staff flag)

## Goal

Restrict product write to staff; orders for authenticated users.

## Concept (5 min)

request.user.is_staff
IsAdminUser vs custom permission class

## Backend steps

- Product create/update/delete: staff only
- Orders: authenticated owner

## Frontend steps

- Hide admin buttons for non-staff
- Still enforce on API (UI hide is not security)

## Check

- [ ] Non-staff gets 403 on product write
- [ ] Staff can manage catalog

## Common bugs

- Trusting only frontend role checks
