# Create View — Write a New Post

## Goal
Add a form so anyone can write and submit a new post

## How Forms Work in Django

```
User fills form → clicks Submit
      ↓
POST /new/  →  PostCreateView
      ↓
Django validates form data
      ↓
Save Post to database
      ↓
Redirect to homepage
```

## 📝 Create `board/forms.py` (new file)

```python
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['title', 'content']
```

| Line | What it does |
|------|-------------|
| `ModelForm` | Auto-generates form fields from the model |
| `fields = ['title', 'content']` | Show only these two fields (not dates) |

## 📝 Edit `board/views.py`

**Update** the import line:

```python
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
```

**Add** after `PostDetailView`:

```python
class PostCreateView(CreateView):
    model         = Post
    form_class    = PostForm
    template_name = 'board/post_form.html'
    success_url   = reverse_lazy('post_list')
```

| Line | What it does |
|------|-------------|
| `form_class = PostForm` | Use our custom form |
| `success_url` | Where to redirect after successful save |
| `reverse_lazy('post_list')` | Generates the URL for the post list |

## 📝 Edit `board/urls.py`

**Add** to `urlpatterns`:

```python
path('new/', views.PostCreateView.as_view(), name='post_create'),
```

## 📝 Create `board/templates/board/post_form.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>New Post</title>
</head>
<body>
    <a href="{% url 'post_list' %}">← Back</a>
    <h1>New Post</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

| Tag | What it does |
|-----|-------------|
| `method="post"` | Send form data to Django (not visible in URL) |
| `{% csrf_token %}` | Security token — **always required** for forms |
| `{{ form.as_p }}` | Render each form field as a `<p>` block |

> Visit `/new/` → fill the form → submit → should redirect to homepage with new post ✅
