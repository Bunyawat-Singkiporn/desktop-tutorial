# S10 — Detail + Create (GET one / POST)

## Goal

Add retrieve-one and create endpoints.

## Concept (5 min)

GET /api/tasks/1/ = one object
POST /api/tasks/ = create with JSON body
201 Created on success

## Backend steps

- Add retrieve route by pk
- Add create; validate title required
- Test POST with Thunder Client

## Frontend steps

- Still no React — API client only

## Check

- [ ] GET detail works
- [ ] POST creates row visible in Admin

## Common bugs

- Sending form-urlencoded instead of JSON
- Missing CSRF on session auth — use Token/JWT or AllowAny for now
