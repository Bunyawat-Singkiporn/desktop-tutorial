# S05 — ERD by hand (Shop: 1:1, 1:N, N:M)

## Goal

Draw an ERD for a mini shop with correct relationship types.

## Concept (5 min)

**1:1** — User <-> Profile
**1:N** — Category -> many Products
**N:M** — Order <-> Product (via OrderLine join table)

## Backend steps

- Entities: Category, Product, Order, OrderLine, Customer
- Draw boxes + lines; label 1:N / N:M

## Frontend steps

- Optional: redraw the same ERD in draw.io

## Check

- [ ] ERD shows at least one 1:N and one N:M (with join table)
- [ ] Every box has a PK

## Common bugs

- Drawing N:M without a join table
