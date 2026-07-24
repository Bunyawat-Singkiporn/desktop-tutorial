from django import forms
from .models import Post

_INPUT    = 'w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400'
_TEXTAREA = _INPUT + ' h-40 resize-none'


class PostForm(forms.ModelForm):
    class Meta:
        model   = Post
        fields  = ['title', 'content']
        widgets = {
            'title':   forms.TextInput(attrs={
                'class':       _INPUT,
                'placeholder': 'Post title...',
            }),
            'content': forms.Textarea(attrs={
                'class':       _TEXTAREA,
                'placeholder': 'Write your post here...',
            }),
        }
