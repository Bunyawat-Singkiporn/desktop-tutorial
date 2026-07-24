# S02 — HTTP: Method, Status, Headers, JSON

## Goal

Read an HTTP exchange and recognize method, status, and JSON body.

## Concept (5 min)

**Methods:** GET (read), POST (create), PUT/PATCH (update), DELETE
**Status:** 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error
**JSON:** data format APIs use — `{ "name": "Ada" }`

## Backend steps

- Open DevTools -> Network; click one request
- Write down: method, status, Content-Type

## Frontend steps

- Paste sample JSON and identify keys/values

## Check

- [ ] List 4 methods and what they mean
- [ ] Match status codes 200 / 400 / 401 / 404

## Common bugs

- Confusing PUT vs PATCH — PATCH = partial update
