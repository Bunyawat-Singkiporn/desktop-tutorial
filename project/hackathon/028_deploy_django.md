# � Deploy Django Backend — Render + Supabase (Free)

**Stack:** Next.js (Vercel) + Django (Render) + Supabase (PostgreSQL)

```
User's Browser
      │
      ▼
┌─────────────────┐          ┌──────────────────────┐
│     Vercel      │  fetch   │       Render         │
│   (Next.js)     │─────────►│     (Django API)     │
│   Frontend      │          └──────────┬───────────┘
└─────────────────┘                     │
                              ┌─────────▼──────────┐
                              │     Supabase       │
                              │   (PostgreSQL)     │
                              └────────────────────┘
```

---

## Part 1 — Set Up Supabase (Database)

### Step 1 — Create Supabase Project

1. Go to [https://supabase.com](https://supabase.com) → Login with GitHub
2. Click **New Project** → fill in name, password, region
3. Wait ~3 minutes for setup
4. Go to **Settings → Database**
5. Scroll to **Connection string → URI** → Copy it

It looks like:
```
postgresql://postgres:[YOUR-PASSWORD]@db.xxxx.supabase.co:5432/postgres
```

> ⚠️ Keep this URL secret — treat it like a password

---

## Part 2 — Prepare Django for Production

### Step 2 — Install Production Packages

```bash
cd backend
pip install gunicorn whitenoise dj-database-url psycopg2-binary
pip freeze > requirements.txt
```

### Step 3 — Create `Procfile`

Create `backend/Procfile` (no extension):
```
web: gunicorn config.wsgi --log-file -
```

### Step 4 — Update `config/settings.py`

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
    "https://your-frontend.vercel.app",  # ← Update after Vercel deploy
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

### Step 5 — Update `.env` for Local Dev with Supabase

```
SECRET_KEY=any-local-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.xxxx.supabase.co:5432/postgres
```

### Step 6 — Run Migrations Locally (Test Connection)

```bash
python manage.py migrate
```

If successful → Django is connected to Supabase. ✅

### Step 7 — Push to GitHub

```bash
git add .
git commit -m "Setup production Django"
git push
```

---

## Part 3 — Deploy Django on Render

### Step 8 — Create Render Account

1. Go to [https://render.com](https://render.com) → **Sign Up with GitHub**

### Step 9 — Create Web Service

1. Click **New → Web Service**
2. Connect your GitHub repo
3. Configure:

| Setting | Value |
|---------|-------|
| **Root Directory** | `backend` |
| **Runtime** | `Python` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn config.wsgi --log-file -` |
| **Instance Type** | `Free` |

### Step 10 — Set Environment Variables

In Render → your service → **Environment**:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Run locally: `python -c "import secrets; print(secrets.token_urlsafe(50))"` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-service.onrender.com` |
| `DATABASE_URL` | Supabase URI (from Step 1) |

### Step 11 — Deploy & Run Migrations

Click **Deploy**. After deploy succeeds, open **Shell** tab in Render:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Step 12 — Get Your Live URL

Render gives you a URL like:
```
https://my-startup-api.onrender.com
```

Test it:
```
https://my-startup-api.onrender.com/api/products/
```

---

## Part 4 — Connect Frontend to Backend

### Step 13 — Update Vercel Environment Variable

1. Go to Vercel → your project → **Settings → Environment Variables**
2. Set `NEXT_PUBLIC_API_URL` = `https://my-startup-api.onrender.com`
3. **Redeploy** from Vercel dashboard

---

## ⚠️ Render Free Tier Note

Render free web services **sleep after 15 minutes** of inactivity. The first request after sleep takes ~30 seconds to wake up. This is fine for demos and hackathons.

---

## ✅ Checklist

- [ ] Supabase project created, URI copied
- [ ] Production packages installed (gunicorn, whitenoise, dj-database-url, psycopg2-binary)
- [ ] `Procfile` created
- [ ] `settings.py` updated for production
- [ ] Local migration to Supabase successful
- [ ] Pushed to GitHub
- [ ] Render web service created
- [ ] Environment variables set on Render
- [ ] Deployed successfully on Render
- [ ] Migrations ran on Render
- [ ] API accessible at `https://your-service.onrender.com/api/`
- [ ] Vercel updated with Render URL
- [ ] Full stack working end-to-end ✅
