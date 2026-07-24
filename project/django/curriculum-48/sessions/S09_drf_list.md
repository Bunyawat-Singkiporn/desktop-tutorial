# S09 — DRF: Serializer + List API (GET /api/items/)

## Goal

Expose a list of model rows as JSON via DRF.

## Concept (5 min)

Serializer = Model <-> JSON.
List API = GET collection endpoint.
Prefer ViewSet or ListAPIView for class.

## Backend steps

- pip install djangorestframework (if not in starter)
- Add rest_framework to INSTALLED_APPS
- Serializer for Task
- GET /api/tasks/ returns JSON array

## Frontend steps

- Open /api/tasks/ in browser or Thunder Client

## Check

- [ ] JSON list matches Admin data
- [ ] Status 200

## Common bugs

- Forgot DEFAULT permissions blocking browse
- Circular import in urls
