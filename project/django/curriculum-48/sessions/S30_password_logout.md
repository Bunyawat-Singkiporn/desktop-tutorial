# S30 — Change password / logout

## Goal

Change password via API; logout on the client.

## Concept (5 min)

Logout with JWT = delete token client-side (and optional blacklist refresh).
Change password: verify old password first.

## Backend steps

- Change-password endpoint
- Optional: refresh token blacklist

## Frontend steps

- Logout clears token + redirect
- Change password form

## Check

- [ ] Logout prevents further API calls
- [ ] Password change works then re-login

## Common bugs

- Only clearing UI state but leaving token
