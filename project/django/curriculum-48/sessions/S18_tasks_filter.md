# S18 — Tasks table with ?status= filter

## Goal

Filter list with query params.

## Concept (5 min)

GET /api/tasks/?status=todo
Query params are part of the URL, not the body.

## Backend steps

- Filter queryset by request.GET.get('status')
- Document allowed values

## Frontend steps

- Filter buttons or select on Tasks page
- Change URL search params and refetch

## Check

- [ ] Filter todo/done works
- [ ] Clear filter shows all

## Common bugs

- Forgetting to reset page when combining with pagination later
