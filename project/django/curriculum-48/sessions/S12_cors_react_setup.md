# S12 — CORS + React Vite + Tailwind first run

## Goal

Run React frontend alongside Django and fix CORS.

## Concept (5 min)

Browsers block cross-origin API calls unless the server allows them.
django-cors-headers + CORS_ALLOWED_ORIGINS for http://localhost:5173

## Backend steps

- Install/enable django-cors-headers
- Allow http://localhost:5173
- Confirm /api/tasks/ still works

## Frontend steps

- Use course starter/frontend or: npm create vite@latest
- Add Tailwind per Vite guide
- npm run dev on :5173
- Show a Hello page

## Check

- [ ] Both servers running
- [ ] No CORS error in console for a test fetch

## Common bugs

- Typo in CORS origin
- Calling http vs https mismatch
