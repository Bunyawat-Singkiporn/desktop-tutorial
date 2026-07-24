# S17 — Dashboard page: aggregate stats API

## Goal

Build a dashboard that shows counts from a stats endpoint.

## Concept (5 min)

Not every page is a table — dashboards need aggregates.
Example: GET /api/tasks/stats/ -> { total, done, todo }

## Backend steps

- Add stats action on ViewSet or separate view
- Use Count / filter in queryset

## Frontend steps

- Dashboard page with 3 cards: Total / Done / Todo
- fetch stats on load

## Check

- [ ] Numbers match reality in Admin

## Common bugs

- Heavy client-side counting when server can aggregate
