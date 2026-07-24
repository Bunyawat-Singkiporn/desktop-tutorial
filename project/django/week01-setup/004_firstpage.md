# Your First Page

## Goal
Write a view and see it live in the browser

## How Django Handles a URL

```
Browser visits /
      ↓
config/urls.py   → routes to board/urls.py
      ↓
board/urls.py    → calls home_view
      ↓
board/views.py   → returns HTML to browser
      ↓
Browser shows the page
```

## 📝 Edit `board/views.py`

```python
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello, Django! 🎉</h1>")
```

| Part | What it does |
|------|-------------|
| `request` | Info about the browser's request (URL, method, user, etc.) |
| `HttpResponse(...)` | Send HTML back to the browser |

## 📝 Create `board/urls.py` (new file)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
]
```

| Part | What it does |
|------|-------------|
| `path('', ...)` | Match the root URL `/` |
| `views.home_view` | Which function to call |
| `name='home'` | A shortcut name (use in templates) |

## 📝 Edit `config/urls.py`

Add `include` import and connect the board app:

```python
from django.contrib import admin
from django.urls import path, include       # ← add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),        # ← add this line
]
```

## Run the Server

```bash
python manage.py runserver
```

Open: **http://127.0.0.1:8000/**

> You should see: **Hello, Django! 🎉** in the browser

## Bonus
Change the message in `home_view` and refresh — see it update instantly.
