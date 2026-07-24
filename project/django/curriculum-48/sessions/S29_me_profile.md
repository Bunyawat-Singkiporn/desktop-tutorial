# S29 — /api/me/ profile page

## Goal

Show the current user from the access token.

## Concept (5 min)

GET /api/me/ uses request.user
No user id in URL — identity comes from token

## Backend steps

- Me view returning id, username, email

## Frontend steps

- Profile page fetching /api/me/
- Show username in navbar

## Check

- [ ] Correct user shown after login

## Common bugs

- Trusting user id from query string instead of request.user
