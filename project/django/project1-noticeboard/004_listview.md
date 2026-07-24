# List View — Show All Posts

## Goal
Build the homepage that shows all posts from the database

## How Django Processes This Request

```
GET /
  ↓
board/urls.py  →  PostListView
  ↓
PostListView   →  queries all Posts from DB
  ↓
post_list.html →  loops through posts, renders HTML
  ↓
Browser shows the page
```

## What is a Class-Based View?

Instead of writing all the logic yourself, Django's built-in views handle it:

```python
# ListView automatically:
# 1. Queries Post.objects.all()
# 2. Passes results to the template as 'posts'
# 3. Returns the rendered HTML
class PostListView(ListView):
    model = Post
    ...
```

## 📝 Edit `board/views.py`

**Replace** the file with:

```python
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    model               = Post
    template_name       = 'board/post_list.html'
    context_object_name = 'posts'
```

| Line | What it does |
|------|-------------|
| `model = Post` | Query this table |
| `template_name` | Which HTML file to render |
| `context_object_name = 'posts'` | Variable name in the template |

## 📝 Edit `board/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
]
```

## 📝 Create `board/templates/board/post_list.html`

First, create the folders:
```bash
mkdir -p board/templates/board
```

Then create the file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Notice Board</title>
</head>
<body>
    <h1>Notice Board</h1>
    <a href="/new/">+ New Post</a>

    {% for post in posts %}
        <div>
            <h2>{{ post.title }}</h2>
            <p>{{ post.created_at }}</p>
        </div>
    {% empty %}
        <p>No posts yet.</p>
    {% endfor %}
</body>
</html>
```

| Template tag | What it does |
|-------------|-------------|
| `{% for post in posts %}` | Loop through all posts |
| `{{ post.title }}` | Display the post's title |
| `{{ post.created_at }}` | Display the date |
| `{% empty %}` | Shown when `posts` is empty |
| `{% endfor %}` | End the loop |

> Run server → visit `/` — should see your 3 test posts listed ✅
