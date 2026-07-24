# S28 — Protected routes + Authorization header

## Goal

Block React routes and API calls without a token.

## Concept (5 min)

DRF: IsAuthenticated
React: wrapper route checking token
api client attaches Authorization: Bearer <access>

## Backend steps

- Set default permission IsAuthenticated on task APIs
- Confirm 401 without token

## Frontend steps

- Auth header in client.js
- Redirect to /login when missing token

## Check

- [ ] With token: 200
- [ ] Without: 401 + redirect

## Common bugs

- Expired token — mention refresh endpoint exists
