# S47 — Deploy basics / production-like checklist

## Goal

Prepare a local production-like checklist; mention PostgreSQL.

## Concept (5 min)

DEBUG=False, SECRET_KEY from env, ALLOWED_HOSTS,
CORS origins, collectstatic if needed,
SQLite ok for class; PostgreSQL for real deploy.

## Backend steps

- Move secrets to environment variables
- Document run instructions in project README

## Frontend steps

- Build frontend: npm run build (discuss serving options)

## Check

- [ ] Checklist filled
- [ ] App still runs with safer settings locally

## Common bugs

- Committing .env with secrets
