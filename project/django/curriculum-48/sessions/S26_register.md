# S26 — Register API + Register page

## Goal

Create a user via API and a Register form in React.

## Concept (5 min)

POST /api/auth/register/ { username, password }
Never return password hashes to client

## Backend steps

- Register serializer + view
- Create User; return 201 + public fields

## Frontend steps

- Register page
- On success navigate to login

## Check

- [ ] New user appears in Admin
- [ ] Weak/empty password rejected

## Common bugs

- Returning password in response
