# Create the Django Project

## Goal
Generate the project folder structure with one command

## Commands

```bash
django-admin startproject config .
python manage.py startapp board
```

> The `.` means "create in the **current folder**" — don't forget it!

## What Was Created?

```
your-folder/
├── manage.py              ← Command center
├── config/
│   ├── settings.py        ← App settings
│   ├── urls.py            ← Main URL router
│   ├── wsgi.py            ← For deployment
│   └── asgi.py            ← For deployment
└── board/
    ├── models.py          ← Database tables
    ├── views.py           ← Page logic
    ├── admin.py           ← Admin panel setup
    └── apps.py            ← App config
```

## What Each File Does

| File | Job |
|------|-----|
| `manage.py` | Run commands: `runserver`, `migrate`, `createsuperuser` |
| `settings.py` | Configure database, installed apps, templates |
| `config/urls.py` | Match URL → app |
| `board/models.py` | Define database tables (classes) |
| `board/views.py` | Logic that runs when a URL is visited |

## 📝 Edit `config/settings.py`

Add `'board'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',    # ← add this line
]
```

## Run the initial migration

```bash
python manage.py migrate
```

This sets up Django's built-in database tables (users, sessions, etc.).

> No errors? ✅ Move to `004_firstpage.md`
