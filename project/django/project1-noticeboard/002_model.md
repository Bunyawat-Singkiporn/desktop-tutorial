# The Post Model

## Goal
Define the `Post` database table using a Python class

## What is a Model?

In Django, a **Model** is a Python class → becomes a database table.

```
class Post (models.Model)
        ↓
  database table: board_post
  columns: id | title | content | created_at | updated_at
```

Django automatically adds the `id` column (primary key).

## Model Field Types

| Field | Stores | Notes |
|-------|--------|-------|
| `CharField(max_length=200)` | Short text | Has a length limit |
| `TextField()` | Long text | No length limit |
| `DateTimeField(auto_now_add=True)` | Date + time when created | Set once, never changes |
| `DateTimeField(auto_now=True)` | Date + time last saved | Updates every time you save |

## 📝 Edit `board/models.py`

```python
from django.db import models


class Post(models.Model):
    title      = models.CharField(max_length=200)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']   # newest post first

    def __str__(self):
        return self.title            # show title in admin
```

## Apply the Model to the Database

Run these two commands every time you change `models.py`:

```bash
python manage.py makemigrations
python manage.py migrate
```

| Command | What it does |
|---------|-------------|
| `makemigrations` | Creates a "recipe" file describing the DB change |
| `migrate` | Applies the recipe to the actual database file |

## Verify it worked

```bash
python manage.py shell
```

```python
from board.models import Post
Post.objects.all()   # should return: <QuerySet []>
exit()
```

> Empty QuerySet = Post table exists and is empty ✅
