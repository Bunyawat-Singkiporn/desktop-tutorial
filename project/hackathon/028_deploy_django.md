# 🚂 Deploy Django Backend to Railway

---

## Why Railway?

**Railway** is the easiest platform to deploy Django backends with a free-tier database.

| Platform | Free Tier | Difficulty |
|----------|-----------|------------|
| **Railway** | $5 credit/month | ⭐ Easy |
| Render | 750 hrs/month | ⭐ Easy |
| Fly.io | Limited free | ⭐⭐ Medium |

---

## Step 1 — Install Production Packages

```bash
cd backend
venv\Scripts\activate    # Windows
# or: source venv/bin/activate  (Mac/Linux)

pip install gunicorn whitenoise psycopg2-binary python-decouple dj-database-url
pip freeze > requirements.txt
```

| Package | Purpose |
|---------|---------|
| `gunicorn` | Production web server (replaces `runserver`) |
| `whitenoise` | Serve static files without a separate server |
| `psycopg2-binary` | Connect Django to PostgreSQL |
| `python-decouple` | Read settings from environment variables |
| `dj-database-url` | Parse `DATABASE_URL` into Django format |

---

## Step 2 — Update `config/settings.py`

Replace the top of the file:

```python
from decouple import config
import dj_database_url

# Security
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1",
    cast=lambda v: [s.strip() for s in v.split(",")]
)
```

**Update MIDDLEWARE** (Whitenoise must be right after SecurityMiddleware):

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",    # ← Add here
    # ... rest unchanged ...
]
```

**Update DATABASES** (supports both SQLite locally and PostgreSQL in production):

```python
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="sqlite:///db.sqlite3")
    )
}
```

**Add static files settings:**

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

**Update CORS** to include your Vercel URL:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-project.vercel.app",    # ← Add after Vercel deploy
]
```

---

## Step 3 — Create a `Procfile`

Create a file named **`Procfile`** (no extension) inside `backend/`:

```
web: gunicorn config.wsgi --log-file -
```

> Railway reads this file to know how to start your server.

---

## Step 4 — Create `.env` for Local Development

Create `backend/.env`:
```
SECRET_KEY=any-random-string-for-local-dev
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Make sure `.env` is in `backend/.gitignore`:
```
venv/
__pycache__/
*.pyc
db.sqlite3
.env          ← never commit this!
```

---

## Step 5 — Push to GitHub

```bash
cd ..    # go back to my-startup root
git add .
git commit -m "Prepare Django for production deploy"
git push
```

---

## Step 6 — Create a Railway Account

1. Go to [https://railway.app](https://railway.app)
2. Click **Login** → **Login with GitHub**
3. Authorize Railway

---

## Step 7 — Create a New Project

1. Click **New Project**
2. Choose **Deploy from GitHub repo**
3. Select your `my-startup` repository
4. Click **Deploy Now**

---

## Step 8 — Configure the Service

Click on the service that was created → **Settings** tab:

| Setting | Value |
|---------|-------|
| **Root Directory** | `backend` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn config.wsgi --log-file -` |

---

## Step 9 — Add a PostgreSQL Database

1. In your project, click **New** → **Database** → **PostgreSQL**
2. Railway creates the database and **automatically** adds `DATABASE_URL` to your service's environment variables

---

## Step 10 — Set Environment Variables

In your service → **Variables** tab, add:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | A long random string (see below) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-project.railway.app` |

**Generate a secure SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

> `DATABASE_URL` is already set automatically by Railway — don't touch it.

---

## Step 11 — Deploy & Run Migrations

Click **Deploy**. Watch the build logs — wait for:
```
✅ Deploy Successful
```

Then run migrations. In Railway → your service → **Settings → Deploy → Post Deploy Command**:
```
python manage.py migrate
```

Or use the **Shell** tab to run manually:
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## Step 12 — Get Your Live URL

In Railway → your service → **Settings → Networking** → click **Generate Domain**

Your API is now live at:
```
https://your-project.railway.app/api/products/
https://your-project.railway.app/admin/
```

---

## Step 13 — Update Vercel with the Backend URL

1. Go to Vercel → your project → **Settings → Environment Variables**
2. Set `NEXT_PUBLIC_API_URL` = `https://your-project.railway.app`
3. Redeploy from Vercel dashboard

---

## Final Architecture

```
User's Browser
      │
      ▼
┌─────────────────┐          ┌──────────────────────┐
│     Vercel      │  fetch   │       Railway        │
│   (Next.js)     │─────────►│   (Django + DRF)     │
│   Frontend      │          │     Backend API      │
└─────────────────┘          └──────────┬───────────┘
                                        │
                              ┌─────────▼──────────┐
                              │    PostgreSQL       │
                              │    Database        │
                              └────────────────────┘
```

---

## ✅ Checklist

- [ ] Production packages installed (`gunicorn`, `whitenoise`, `psycopg2`, etc.)
- [ ] `settings.py` updated (SECRET_KEY from env, Whitenoise, dj-database-url)
- [ ] `Procfile` created
- [ ] `.env` created for local dev + added to `.gitignore`
- [ ] Pushed to GitHub
- [ ] Railway account created
- [ ] Service configured (Root Directory = `backend`)
- [ ] PostgreSQL database added
- [ ] Environment variables set (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
- [ ] Deployed successfully
- [ ] Migrations run on production
- [ ] Live URL working (`/api/products/`)
- [ ] Vercel updated with Railway URL
- [ ] Full stack working end-to-end 🎉
