# Detail View — Single Post Page

## Goal
Click a post title to open and read the full content

## 📝 Edit `board/views.py`

**Update** the import line:

```python
from django.views.generic import ListView, DetailView
```

**Add** after `PostListView`:

```python
class PostDetailView(DetailView):
    model         = Post
    template_name = 'board/post_detail.html'
```

`DetailView` automatically fetches `Post.objects.get(pk=<id from URL>)` and passes it to the template as `post`.

## 📝 Edit `board/urls.py`

**Add** to `urlpatterns`:

```python
path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
```

| URL part | Meaning |
|---------|---------|
| `<int:pk>` | Capture a number from the URL |
| `pk` | "Primary Key" — the post's unique ID |

So `/post/3/` → fetches Post with id=3.

## 📝 Create `board/templates/board/post_detail.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <a href="{% url 'post_list' %}">← Back</a>
    <h1>{{ post.title }}</h1>
    <p>{{ post.created_at }}</p>
    <hr>
    <p>{{ post.content }}</p>
</body>
</html>
```

| Template tag | What it does |
|-------------|-------------|
| `{% url 'post_list' %}` | Generate the URL `/` using its name |
| `{{ post.content }}` | Display full content |

## 📝 Update `post_list.html` — make titles clickable

**Replace** `<h2>{{ post.title }}</h2>` with:

```html
<h2>
    <a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a>
</h2>
```

`{% url 'post_detail' post.pk %}` → generates `/post/1/`, `/post/2/`, etc.

> Click a post title → should open the detail page ✅
