# Deploy to Railway

## Goal
Put the Notice Board online so anyone with the URL can use it

## Step 1 — Push to GitHub

Make sure your project is in a GitHub repository.

```bash
git init
git add .
git commit -m "Notice Board complete"
git push origin main
```

## Step 2 — Update `config/settings.py` for production

**Add** at the top:
```python
import os
```

**Replace or update** these lines:

```python
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-only-change-this')
DEBUG      = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']
```

**Add** `whitenoise` to MIDDLEWARE (second position):

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ← add this
    ...rest of list...
]
```

**Add** at the bottom:

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## Step 3 — Create `Procfile` (no file extension)

```
web: gunicorn config.wsgi --log-file -
```

## Step 4 — Update `requirements.txt`

```bash
pip freeze > requirements.txt
```

Or write manually:
```
Django>=5.0,<6.0
gunicorn
whitenoise
psycopg2-binary
```

## Step 5 — Collect static files

```bash
python manage.py collectstatic
```

## Step 6 — Deploy on Railway

1. Go to **railway.app** → Sign in with GitHub
2. **New Project** → **Deploy from GitHub repo**
3. Select your repository
4. Add environment variable:
   - Key: `SECRET_KEY`
   - Value: any random 50-character string
5. Railway auto-detects Django → deploys automatically

## Step 7 — Run migrations on Railway

In Railway dashboard → your service → **New Command**:

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Done 🎉

Railway gives you a URL like:
```
https://your-app-name.up.railway.app
```

Share it with anyone!
