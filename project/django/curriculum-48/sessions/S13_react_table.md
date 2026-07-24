# S13 — fetch list -> simple table page

## Goal

Build a Tasks table page that loads from GET /api/tasks/.

## Concept (5 min)

useEffect + fetch on mount.
Map JSON array to <table> or Tailwind rows.

## Backend steps

- Ensure list endpoint AllowAny or provide token later

## Frontend steps

- Create TasksPage
- fetch(`${API}/api/tasks/`)
- Render title + done columns
- Route /tasks

## Check

- [ ] Table shows same rows as Admin
- [ ] Loading state optional

## Common bugs

- Forgetting await / .json()
- Hardcoding wrong API base URL
