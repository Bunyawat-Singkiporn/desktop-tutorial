# S07 — Django refresh: project, app, settings, urls, runserver

## Goal

Create/run a Django project and hit a hello URL.

## Concept (5 min)

**Project** = whole site (settings, root urls)
**App** = one feature module
`runserver` = local development server

## Backend steps

- Use course starter or: django-admin startproject config .
- python manage.py startapp core
- Wire urls -> simple view returning HttpResponse or JsonResponse
- python manage.py runserver

## Frontend steps

- Visit http://127.0.0.1:8000/ and confirm response

## Check

- [ ] Server runs without error
- [ ] Can explain project vs app

## Common bugs

- Wrong venv / Django not installed
- Editing the wrong urls.py
