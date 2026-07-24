# S25 — Auth concepts: session vs token vs JWT

## Goal

Choose JWT for this course and know why.

## Concept (5 min)

**Session:** cookie on browser; server stores session
**Token:** key in Authorization header
**JWT:** signed token; access (+ refresh) pattern with SimpleJWT

## Backend steps

- Discuss which fits SPA (React) best — JWT/token
- Install djangorestframework-simplejwt (starter may include)

## Frontend steps

- No UI yet — whiteboard auth flow

## Check

- [ ] Can explain why SPA often uses JWT
- [ ] Draw login -> token -> Authorization header

## Common bugs

- Storing JWT in localStorage vs httpOnly cookie tradeoffs — mention only
