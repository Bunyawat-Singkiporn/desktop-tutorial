# Update + Delete Views

## Goal
Let users edit and delete existing posts

## 📝 Edit `board/views.py`

**Update** the import line:

```python
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
```

**Add** after `PostCreateView`:

```python
class PostUpdateView(UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = 'board/post_form.html'
    success_url   = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model         = Post
    template_name = 'board/post_confirm_delete.html'
    success_url   = reverse_lazy('post_list')
```

`UpdateView` reuses `post_form.html` — the same form works for both create and edit.

## 📝 Edit `board/urls.py`

**Add** to `urlpatterns`:

```python
path('post/<int:pk>/edit/',   views.PostUpdateView.as_view(), name='post_update'),
path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
```

## 📝 Create `board/templates/board/post_confirm_delete.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Delete Post</title>
</head>
<body>
    <h1>Delete "{{ post.title }}"?</h1>
    <p>This cannot be undone.</p>

    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, delete</button>
        <a href="{% url 'post_detail' post.pk %}">Cancel</a>
    </form>
</body>
</html>
```

## 📝 Update `post_detail.html` — add Edit and Delete buttons

**Add** before `</body>`:

```html
<a href="{% url 'post_update' post.pk %}">Edit</a>
<a href="{% url 'post_delete' post.pk %}">Delete</a>
```

## Full URL map so far

| URL | View | Name |
|-----|------|------|
| `/` | PostListView | `post_list` |
| `/post/<id>/` | PostDetailView | `post_detail` |
| `/new/` | PostCreateView | `post_create` |
| `/post/<id>/edit/` | PostUpdateView | `post_update` |
| `/post/<id>/delete/` | PostDeleteView | `post_delete` |

> Test all 5 URLs — create, read, edit, delete all working ✅
