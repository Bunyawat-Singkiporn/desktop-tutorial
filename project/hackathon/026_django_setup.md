# 🐍 Django Backend Setup — Step by Step

---

## What is Django?

**Django** is a Python web framework for building backends and APIs quickly.

| Feature | Benefit |
|---------|---------|
| Built-in Admin Panel | Manage your database without writing code |
| Django REST Framework | Turn your models into a JSON API easily |
| ORM | Write Python instead of SQL |
| Security Built-in | CSRF protection, SQL injection prevention |

---

## Prerequisites

**Python 3.10+** must be installed.

```bash
python --version    # should show 3.10 or higher
```

---

## Step 1 — Create the Backend Folder

```bash
cd my-startup
mkdir backend
cd backend
```

---

## Step 2 — Create a Virtual Environment

A virtual environment keeps your project's packages isolated from other projects.

```bash
python -m venv venv
```

**Activate it:**

| OS | Command |
|----|---------|
| Windows | `venv\Scripts\activate` |
| Mac / Linux | `source venv/bin/activate` |

You should see `(venv)` at the start of your terminal line.

> ⚠️ Always activate the venv before working on this project!

---

## Step 3 — Install Django and Required Packages

```bash
pip install django djangorestframework django-cors-headers python-decouple dj-database-url psycopg2-binary
```

| Package | Purpose |
|---------|---------|
| `django` | The core framework |
| `djangorestframework` | Build JSON APIs |
| `django-cors-headers` | Allow Next.js frontend to call your API |
| `python-decouple` | Read settings from a `.env` file |
| `dj-database-url` | Convert DATABASE_URL string to Django format |
| `psycopg2-binary` | Connect to PostgreSQL (for Supabase) |

**Save dependencies to a file:**
```bash
pip freeze > requirements.txt
```

---

## Step 4 — Create a Django Project

```bash
django-admin startproject config .
```

> The `.` at the end means "create in the current folder" — keeps the structure clean.

**Folder structure so far:**
```
backend/
├── config/
│   ├── settings.py     ← All project settings
│   ├── urls.py         ← Main URL routing
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── venv/
```

---

## Step 5 — Set Up Environment Variables

Create `backend/.env` **(choose one option below)**:

### Option A: SQLite (Simple, Local Only)

For local development without a shared database:

```
SECRET_KEY=your-local-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Option B: Supabase PostgreSQL (Team-Friendly)

For multiple developers sharing one database:

**Step 1: Create a Supabase project**
1. Go to [https://supabase.com](https://supabase.com)
2. Click **New Project**
3. Choose a name, password, and region
4. Click **Create**
5. Wait ~3 minutes for the database to spin up

**Step 2: Get your connection string**
1. In Supabase → **Settings → Database**
2. Copy the connection string under "PostgreSQL URI"
3. It looks like: `postgresql://user:password@host:5432/postgres`

**Step 3: Add to `.env`**

```
SECRET_KEY=your-local-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@host:5432/postgres
```

---

**Add `.env` to `.gitignore`** so it never gets pushed to GitHub:

```
venv/
__pycache__/
*.pyc
db.sqlite3
.env
```

Now update the **top of `config/settings.py`** to read from `.env`:

```python
import dj_database_url
from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1",
    cast=lambda v: [s.strip() for s in v.split(",")]
)

# Database: supports both SQLite and PostgreSQL
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="sqlite:///db.sqlite3")
    )
}
```

> All teammates create their own `.env` locally — secrets never go into GitHub. 
> If using Supabase, each person points to the **same DATABASE_URL** from Supabase.

---

## Step 5.5 — Update DATABASES in settings.py

Make sure your `config/settings.py` has this **DATABASES** section (add if not present):

```python
# Around line 80-100, find DATABASES = { ... } and replace with:

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="sqlite:///db.sqlite3")
    )
}
```

This lets Django read **DATABASE_URL** from `.env` automatically.

---

## Step 6 — Create an App

In Django, an **app** is a module that handles one part of your project (e.g., products, users, orders).

```bash
python manage.py startapp products
```

**Register the app in `config/settings.py`:**
```python
INSTALLED_APPS = [
    # ... default apps ...
    "rest_framework",
    "corsheaders",
    "products",          # ← Add this
]
```

**Add CORS middleware in `config/settings.py`:**
```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",   # ← Must be at the TOP
    "django.middleware.security.SecurityMiddleware",
    # ... rest of middleware ...
]

# Allow Next.js frontend to call this API
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

---

## Step 7 — Create a Model

A **model** is a Python class that becomes a table in the database.

Open `products/models.py`:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

**Apply the model to the database:**
```bash
python manage.py makemigrations   # Generate migration files
python manage.py migrate          # Apply to database
```

---

## Step 8 — Register in Admin Panel

Open `products/admin.py`:

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

---

## Step 9 — Create an API Endpoint

**Create `products/serializers.py`:**
```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
```

**Update `products/views.py`:**
```python
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

**Create `products/urls.py`:**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
```

**Register in `config/urls.py`:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("products.urls")),   # ← Add this
]
```

---

## Step 10 — Create Admin User & Run Server

```bash
python manage.py createsuperuser
# Fill in: username, email, password
```

```bash
python manage.py runserver
```

| URL | What you see |
|-----|-------------|
| `http://localhost:8000/api/products/` | JSON API |
| `http://localhost:8000/api/products/1/` | Single item |
| `http://localhost:8000/admin/` | Admin panel |

---

## Step 11 — Test the API

You can test with the browser, or use **Postman** / **Thunder Client** (VS Code extension):

| Method | URL | Action |
|--------|-----|--------|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create new product |
| GET | `/api/products/1/` | Get product with id=1 |
| PUT | `/api/products/1/` | Update product |
| DELETE | `/api/products/1/` | Delete product |

---

## Step 12 — Best Practice Folder Structure

As your project grows, **each Django app should follow this internal structure**:

```
backend/
├── config/                     ← Project-level config (created by startproject)
│   ├── settings.py             ← All settings (reads from .env)
│   ├── urls.py                 ← Root URL router
│   ├── wsgi.py
│   └── asgi.py
├── products/                   ← One app per feature/domain
│   ├── migrations/             ← Auto-generated — do not edit manually
│   ├── tests/                  ← Tests for this app
│   │   └── test_views.py
│   ├── admin.py                ← Register models in admin panel
│   ├── models.py               ← Database tables
│   ├── serializers.py          ← Convert model ↔ JSON
│   ├── views.py                ← Handle requests, return responses
│   ├── urls.py                 ← URL routes for this app
│   └── permissions.py          ← Who can access what (optional)
├── users/                      ← Another app for user/auth logic
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── middleware/                 ← Custom middleware (optional)
│   └── logging_middleware.py
├── .env                        ← Local secrets (never commit!)
├── .env.example                ← Template for teammates (commit this)
├── .gitignore
├── manage.py
├── Procfile                    ← For deployment (gunicorn)
└── requirements.txt
```

### One app per domain — keep it separate

| App | Handles |
|-----|--------|
| `products/` | Product CRUD |
| `users/` | Registration, login, profile |
| `orders/` | Order creation, history |
| `payments/` | Payment records |

> Each app should do **one thing** and be independent.

### Custom Middleware

Middleware runs on **every request** before it reaches the view. Useful for logging, authentication checks, or adding headers.

Create `backend/middleware/logging_middleware.py`:

```python
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view: log the incoming request
        logger.info(f"{request.method} {request.path}")

        response = self.get_response(request)  # Call the view

        # After view: log the response status
        logger.info(f"Response: {response.status_code}")
        return response
```

Register it in `config/settings.py`:

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "middleware.logging_middleware.RequestLoggingMiddleware",  # ← Add here
    # ... rest unchanged ...
]
```

### Custom Permissions

Create `products/permissions.py` to control who can access which endpoint:

```python
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Allow anyone to read (GET).
    Only allow the owner to write (POST, PUT, DELETE).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return obj.owner == request.user
```

Use it in `views.py`:

```python
from .permissions import IsOwnerOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
```

### `.env.example` — commit this file!

Create `backend/.env.example` (safe to commit, no real values):
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

> Teammates clone the repo → copy `.env.example` → rename to `.env` → fill in values.

---

## Step 13 — Push to GitHub

Create `backend/.gitignore`:
```
venv/
__pycache__/
*.pyc
db.sqlite3
.env
```

```bash
cd ..    # go back to my-startup root
git add .
git commit -m "Add Django backend"
git push
```

---

## ✅ Checklist

- [ ] Virtual environment created and activated
- [ ] Django + DRF + CORS installed
- [ ] `requirements.txt` created
- [ ] Project created with `django-admin startproject`
- [ ] `.env` file created with SECRET_KEY, DEBUG, ALLOWED_HOSTS
- [ ] `settings.py` updated to use `python-decouple`
- [ ] `.env` added to `.gitignore`
- [ ] App created with `startapp`
- [ ] App registered in `INSTALLED_APPS`
- [ ] CORS configured
- [ ] `.env.example` created (committed to GitHub)
- [ ] Model created and migrated
- [ ] Admin registered
- [ ] Serializer + ViewSet + URLs created
- [ ] API working at `/api/products/`
- [ ] Admin panel accessible
- [ ] `lib/` folder structure in place (for larger apps)
- [ ] Pushed to GitHub
