# Styling with Tailwind CSS

## Goal
Make the app look clean using Tailwind CSS — no CSS files needed

## What is Tailwind?

Tailwind = utility classes applied directly in HTML.

```html
<!-- plain HTML -->
<button>Save</button>

<!-- Tailwind -->
<button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
    Save
</button>
```

No CSS file. No class naming. Just classes on elements.

## How — Tailwind CDN (zero install)

Add ONE script tag to your HTML `<head>`:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

## 📝 Create `board/templates/board/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Notice Board{% endblock %}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen">

    <nav class="bg-white shadow px-6 py-4 flex justify-between items-center">
        <a href="{% url 'post_list' %}" class="text-xl font-bold text-blue-600">
            📋 Notice Board
        </a>
        <a href="{% url 'post_create' %}"
           class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 text-sm font-medium">
            + New Post
        </a>
    </nav>

    <main class="max-w-3xl mx-auto mt-8 px-4 pb-12">
        {% block content %}{% endblock %}
    </main>

</body>
</html>
```

| Tailwind class | What it does |
|---------------|-------------|
| `bg-gray-100` | Light gray background |
| `max-w-3xl mx-auto` | Center content, max width |
| `flex justify-between` | Navbar items on left and right |
| `hover:bg-blue-600` | Darker on hover |

## 📝 Replace all templates to extend base.html

**`post_list.html`** — replace entire file:

```html
{% extends 'board/base.html' %}
{% block title %}Notice Board{% endblock %}

{% block content %}
    <h1 class="text-2xl font-bold mb-6 text-gray-800">All Posts</h1>

    {% for post in posts %}
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-5 mb-4 hover:shadow-md transition">
            <h2 class="text-xl font-semibold">
                <a href="{% url 'post_detail' post.pk %}" class="text-blue-600 hover:underline">
                    {{ post.title }}
                </a>
            </h2>
            <p class="text-gray-400 text-sm mt-1">{{ post.created_at|date:"M d, Y · H:i" }}</p>
            <p class="text-gray-600 mt-2 text-sm">{{ post.content|truncatewords:20 }}</p>
        </div>
    {% empty %}
        <div class="text-center py-16 text-gray-400">
            <p class="text-lg">No posts yet.</p>
            <a href="{% url 'post_create' %}" class="text-blue-500 hover:underline mt-2 inline-block">
                Create the first one →
            </a>
        </div>
    {% endfor %}
{% endblock %}
```

**`post_detail.html`** — replace entire file:

```html
{% extends 'board/base.html' %}
{% block title %}{{ post.title }}{% endblock %}

{% block content %}
    <a href="{% url 'post_list' %}" class="text-blue-600 hover:underline text-sm">← Back</a>

    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mt-4">
        <h1 class="text-2xl font-bold text-gray-800">{{ post.title }}</h1>
        <p class="text-gray-400 text-sm mt-1">{{ post.created_at|date:"M d, Y · H:i" }}</p>
        <hr class="my-5 border-gray-200">
        <p class="text-gray-700 leading-relaxed whitespace-pre-wrap">{{ post.content }}</p>
        <div class="mt-8 flex gap-3">
            <a href="{% url 'post_update' post.pk %}"
               class="bg-yellow-400 text-white px-4 py-2 rounded hover:bg-yellow-500 text-sm font-medium">
                ✏️ Edit
            </a>
            <a href="{% url 'post_delete' post.pk %}"
               class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 text-sm font-medium">
                🗑️ Delete
            </a>
        </div>
    </div>
{% endblock %}
```

**`post_form.html`** — replace entire file:

```html
{% extends 'board/base.html' %}
{% block title %}{% if form.instance.pk %}Edit Post{% else %}New Post{% endif %}{% endblock %}

{% block content %}
    <h1 class="text-2xl font-bold mb-6 text-gray-800">
        {% if form.instance.pk %}Edit Post{% else %}New Post{% endif %}
    </h1>
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <form method="post">
            {% csrf_token %}
            <div class="mb-5">
                <label class="block text-sm font-semibold text-gray-700 mb-1">Title</label>
                {{ form.title }}
            </div>
            <div class="mb-5">
                <label class="block text-sm font-semibold text-gray-700 mb-1">Content</label>
                {{ form.content }}
            </div>
            <div class="flex items-center gap-4">
                <button type="submit"
                        class="bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-600 font-medium">
                    Save Post
                </button>
                <a href="{% url 'post_list' %}" class="text-gray-500 hover:text-gray-700 text-sm">Cancel</a>
            </div>
        </form>
    </div>
{% endblock %}
```

**`post_confirm_delete.html`** — replace entire file:

```html
{% extends 'board/base.html' %}
{% block title %}Delete Post{% endblock %}

{% block content %}
    <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-8 max-w-md mx-auto mt-8 text-center">
        <div class="text-5xl mb-4">🗑️</div>
        <h1 class="text-xl font-bold text-gray-800 mb-2">Delete this post?</h1>
        <p class="text-gray-500 mb-2 font-medium">"{{ post.title }}"</p>
        <p class="text-gray-400 text-sm mb-8">This action cannot be undone.</p>
        <form method="post">
            {% csrf_token %}
            <div class="flex justify-center gap-4">
                <button type="submit"
                        class="bg-red-500 text-white px-6 py-2 rounded hover:bg-red-600 font-medium">
                    Yes, delete
                </button>
                <a href="{% url 'post_detail' post.pk %}"
                   class="bg-gray-100 text-gray-700 px-6 py-2 rounded hover:bg-gray-200 font-medium">
                    Cancel
                </a>
            </div>
        </form>
    </div>
{% endblock %}
```

## 📝 Update `board/forms.py` — add Tailwind classes to inputs

**Replace** the file with:

```python
from django import forms
from .models import Post

_INPUT    = 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400'
_TEXTAREA = _INPUT + ' h-40 resize-none'


class PostForm(forms.ModelForm):
    class Meta:
        model   = Post
        fields  = ['title', 'content']
        widgets = {
            'title':   forms.TextInput(attrs={'class': _INPUT,    'placeholder': 'Post title...'}),
            'content': forms.Textarea(attrs={ 'class': _TEXTAREA, 'placeholder': 'Write your post here...'}),
        }
```

> Run server → app looks clean and modern ✅
