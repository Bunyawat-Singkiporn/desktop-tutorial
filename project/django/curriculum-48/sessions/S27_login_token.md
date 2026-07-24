# S27 — Login API + store token

## Goal

Login and store access token for later requests.

## Concept (5 min)

POST /api/auth/token/ (SimpleJWT) -> access, refresh
Save access token (localStorage for class simplicity)

## Backend steps

- Wire SimpleJWT urls
- Test token obtain in Thunder Client

## Frontend steps

- Login page
- Save token; redirect to app home

## Check

- [ ] Token returned and stored
- [ ] Bad credentials show error

## Common bugs

- Calling protected API without Bearer prefix
