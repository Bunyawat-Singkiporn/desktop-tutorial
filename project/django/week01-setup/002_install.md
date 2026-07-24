# Install Django

## Goal
Install Django and confirm it works

## Step 1 — Create a virtual environment

```bash
python -m venv venv
```

Activate it:

| OS | Command |
|----|---------|
| Windows | `venv\Scripts\activate` |
| Mac / Linux | `source venv/bin/activate` |

You should see `(venv)` at the start of your terminal line.

## Step 2 — Install Django

```bash
pip install django gunicorn whitenoise
```

| Package | What it's for |
|---------|---------------|
| `django` | The web framework |
| `gunicorn` | Web server for deployment |
| `whitenoise` | Serve static files in production |

## Step 3 — Confirm it worked

```bash
python -m django --version
```

You should see: `5.x.x`

## Step 4 — Save dependencies

```bash
pip freeze > requirements.txt
```

> This file tells Railway (and teammates) which packages to install.

> If you see `5.x.x` — you're ready. Move to `003_project.md` ✅
