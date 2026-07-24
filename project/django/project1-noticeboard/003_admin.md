# Admin Panel

## Goal
Use Django's built-in admin to add test posts without writing a form yet

## What is the Admin Panel?

Django ships with a free dashboard at `/admin/` — add, edit, delete data with zero frontend work.

```
http://127.0.0.1:8000/admin/
```

## Step 1 — Create a superuser

```bash
python manage.py createsuperuser
```

Enter: username, email (optional), password

## 📝 Edit `board/admin.py`

**Replace** the file content with:

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    ordering      = ['-created_at']
```

| Option | What it does |
|--------|-------------|
| `list_display` | Columns shown in the post list |
| `search_fields` | Which fields the search box searches |
| `ordering` | Default sort (`-` = descending = newest first) |

## Run and Check

```bash
python manage.py runserver
```

1. Go to **http://127.0.0.1:8000/admin/**
2. Login with your superuser credentials
3. Click **Posts** → **Add Post**
4. Add **3 test posts**

> You should see your posts listed with title and dates ✅

## Bonus
Try the search box — it searches title and content.
