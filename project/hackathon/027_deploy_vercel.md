# 🚀 Deploy Next.js Frontend to Vercel

---

## What is Vercel?

**Vercel** is the company that made Next.js. They offer free hosting optimized for Next.js.

| Feature | Detail |
|---------|--------|
| Free tier | Generous free plan for small projects |
| Auto HTTPS | SSL certificate out of the box |
| Global CDN | Fast for users worldwide |
| Auto Deploy | Push to GitHub → live in ~1 minute |
| Preview URLs | Every branch gets its own preview link |

---

## Prerequisites

- Next.js project pushed to GitHub ✅
- A Vercel account (free)

---

## Step 1 — Sign Up for Vercel

1. Go to [https://vercel.com](https://vercel.com)
2. Click **Sign Up**
3. Choose **Continue with GitHub**
4. Authorize Vercel to access your GitHub account

---

## Step 2 — Import Your Repository

1. On the Vercel dashboard, click **Add New → Project**
2. Find your repository (e.g. `my-startup`) → Click **Import**
3. Vercel auto-detects it as a Next.js project

---

## Step 3 — Configure Project Settings

> ⚠️ This step is critical if your Next.js app is inside a subfolder (`frontend/`)

Click **Edit** next to **Root Directory** → type `frontend` → click **Continue**

| Setting | Value |
|---------|-------|
| Framework Preset | `Next.js` (auto-detected) |
| **Root Directory** | `frontend` ← set this! |
| Build Command | `npm run build` (default) |
| Output Directory | `.next` (default) |

---

## Step 4 — Set Environment Variables

Click **Environment Variables** and add:

| Name | Value |
|------|-------|
| `NEXT_PUBLIC_API_URL` | `https://your-django-backend.railway.app` |

> You will get the Railway URL after deploying Django (see next file).
> For now you can skip this and add it later.

---

## Step 5 — Deploy

Click **Deploy**.

Vercel will:
1. Pull your code from GitHub
2. Run `npm run build`
3. Deploy to a live URL

Wait ~1–2 minutes. You will see:
```
🎉 Congratulations! Your project has been deployed.
```

Your site is live at: `https://my-startup.vercel.app`

---

## Step 6 — How Auto-Deploy Works

Every time you `git push` to the `main` branch:

```
git push  →  Vercel detects it  →  Runs build  →  Goes live automatically
```

You never need to manually deploy again!

**Preview Deployments:**

When you push to any other branch:
```
git checkout -b feature/new-page
git push origin feature/new-page
```

Vercel creates a **preview URL** (e.g. `my-startup-git-feature-new-page.vercel.app`) so you can test before merging.

---

## Step 7 — Add Environment Variable After Railway Deploy

Once your Django backend is deployed on Railway:

1. Go to Vercel → your project → **Settings → Environment Variables**
2. Add or update:
   ```
   NEXT_PUBLIC_API_URL = https://your-project.railway.app
   ```
3. Go to **Deployments** → click the 3-dot menu on the latest deploy → **Redeploy**

---

## Step 8 — Connect a Custom Domain (Optional)

1. Go to your project on Vercel → **Settings → Domains**
2. Click **Add Domain**
3. Enter your domain (e.g. `mystartup.com`)
4. Copy the DNS records shown and add them in your domain registrar (GoDaddy, Namecheap, etc.)
5. Wait 1–24 hours for DNS propagation

---

## Using Environment Variables in Code

```jsx
// src/app/page.jsx

async function getData() {
  // Uses NEXT_PUBLIC_API_URL from .env.local (dev) or Vercel env vars (production)
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/products/`);
  return res.json();
}
```

Local `.env.local` (for development only, never commit this):
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## ✅ Checklist

- [ ] Vercel account created (via GitHub)
- [ ] Repository imported to Vercel
- [ ] Root Directory set to `frontend`
- [ ] Deployed successfully
- [ ] Live URL working
- [ ] `NEXT_PUBLIC_API_URL` env var set (after Django deploy)
- [ ] Auto-deploy tested (push to main → site updates)
