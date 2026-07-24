# S08 — Model + migrate + Admin (ERD -> Model)

## Goal

Turn one ERD entity into a Model and manage it in Admin.

## Concept (5 min)

Model = Python class that becomes a DB table.
makemigrations = plan changes
migrate = apply changes
Admin = built-in UI for data entry

## Backend steps

- Create model matching ERD (e.g. Task: title, done, created_at)
- makemigrations + migrate
- Register in admin; createsuperuser
- Add 3 rows in Admin

## Frontend steps

- No React yet — Admin is enough for data

## Check

- [ ] Model appears in Admin
- [ ] DB updated after migrate

## Common bugs

- Forgot migrate
- Forgot to register the model in admin.py
