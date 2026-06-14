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
pip install django djangorestframework django-cors-headers
```

| Package | Purpose |
|---------|---------|
| `django` | The core framework |
| `djangorestframework` | Build JSON APIs |
| `django-cors-headers` | Allow Next.js frontend to call your API |

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

## Step 5 — Create an App

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

## Step 6 — Create a Model

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

## Step 7 — Register in Admin Panel

Open `products/admin.py`:

```python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

---

## Step 8 — Create an API Endpoint

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

## Step 9 — Create Admin User & Run Server

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

## Step 10 — Test the API

You can test with the browser, or use **Postman** / **Thunder Client** (VS Code extension):

| Method | URL | Action |
|--------|-----|--------|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create new product |
| GET | `/api/products/1/` | Get product with id=1 |
| PUT | `/api/products/1/` | Update product |
| DELETE | `/api/products/1/` | Delete product |

---

## Step 11 — Push to GitHub

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
- [ ] App created with `startapp`
- [ ] App registered in `INSTALLED_APPS`
- [ ] CORS configured
- [ ] Model created and migrated
- [ ] Admin registered
- [ ] Serializer + ViewSet + URLs created
- [ ] API working at `/api/products/`
- [ ] Admin panel accessible
- [ ] Pushed to GitHub
