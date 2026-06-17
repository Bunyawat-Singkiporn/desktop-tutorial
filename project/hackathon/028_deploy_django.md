# 🚂 Deploy Django Backend

---

## Option A: Railway + PostgreSQL (Recommended)

Railway is simple: push to GitHub, Railway builds & deploys automatically.

### Step 1 — Install Production Packages

```bash
cd backend
pip install gunicorn whitenoise dj-database-url
pip freeze > requirements.txt
```

### Step 2 — Create `Procfile`

Create `backend/Procfile` (no extension):
```
web: gunicorn config.wsgi --log-file -
```

### Step 3 — Update `config/settings.py`

Add these at the top:

```python
from decouple import config
import dj_database_url

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="localhost").split(",")

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="sqlite:///db.sqlite3")
    )
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-domain.vercel.app",
]
```

Add Whitenoise to MIDDLEWARE (right after SecurityMiddleware):
```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ← Add
    # ... rest unchanged
]
```

### Step 4 — Push to GitHub

```bash
git add .
git commit -m "Setup production Django"
git push
```

### Step 5 — Deploy on Railway

1. Go to [https://railway.app](https://railway.app) → Login with GitHub
2. Click **New Project** → **Deploy from GitHub repo**
3. Select your repo → **Deploy**
4. Click the service → **Settings** → set Root Directory to `backend`
5. Click **+ New** → **Database** → **PostgreSQL**
6. Railway adds `DATABASE_URL` automatically

### Step 6 — Set Environment Variables

In Railway → Your service → **Variables**:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | `python -c "import secrets; print(secrets.token_urlsafe(50))"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-project.railway.app` |

> `DATABASE_URL` is already set by PostgreSQL addon

---

## Option B: Supabase + Django

Supabase provides PostgreSQL hosting + built-in auth & real-time features.

### Step 1 — Create Supabase Project

1. Go to [https://supabase.com](https://supabase.com) → **New Project**
2. Name your project, set password, choose region
3. Wait ~3 minutes
4. Go to **Settings** → **Database** → Copy **PostgreSQL URI**
5. It looks like: `postgresql://user:pass@host/postgres`

### Step 2 — Update Django for Supabase

In `backend/.env` (local development):
```
DATABASE_URL=postgresql://user:pass@host/postgres
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Your Django settings already support this (from Step 026).

### Step 3 — Deploy Backend (Railway or Render)

After your Django backend is configured for Supabase:
- Use **Railway** (same as Option A, but skip PostgreSQL addon — use Supabase URL instead)
- Or use **Render** (free tier available)

When setting environment variables, add:
```
DATABASE_URL=postgresql://user:pass@host/postgres
```

---

## After Deployment

**Run migrations on the server:**

In your Railway/Render dashboard, open a Shell:
```bash
python manage.py migrate
python manage.py createsuperuser
```

**Test your API:**
```
https://your-project.railway.app/api/products/
```

**Update frontend `.env.local`:**
```
NEXT_PUBLIC_API_URL=https://your-project.railway.app
```

Then deploy frontend to Vercel (see Step 027).

---

## ✅ Checklist

- [ ] Production packages installed (gunicorn, whitenoise, dj-database-url)
- [ ] `Procfile` created
- [ ] `config/settings.py` updated for production
- [ ] `.env` set for local dev
- [ ] Pushed to GitHub
- [ ] Deployed to Railway (or Render)
- [ ] Database connected (Railway PostgreSQL or Supabase)
- [ ] Environment variables set on server
- [ ] Migrations ran successfully
- [ ] API accessible at `https://your-backend.railway.app/api/`

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
