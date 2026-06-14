# 🐙 GitHub Setup — Version Control for Your Project

---

## What is GitHub?

- **Git** — a tool that tracks changes in your code (runs on your computer)
- **GitHub** — a website that stores your code online and lets teams collaborate

> Think of Git like "Save History" and GitHub like "Google Drive for code"

---

## Step 1 — Create a GitHub Account

1. Go to [https://github.com](https://github.com)
2. Click **Sign up**
3. Enter your email, password, and username
4. Verify your email

---

## Step 2 — Install Git on Your Computer

**Check if Git is already installed:**
```bash
git --version
```

**If not installed:**
- **Windows:** Download from [https://git-scm.com](https://git-scm.com) → Run installer
- **Mac:** Run `xcode-select --install` in Terminal
- **Linux:** Run `sudo apt install git`

**Set up your identity (do this once):**
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

## Step 3 — Create a New Repository on GitHub

1. Click the **+** button (top right) → **New repository**
2. Fill in:
   - **Repository name:** e.g. `my-startup`
   - **Description:** (optional)
   - **Visibility:** Public or Private
   - ✅ Check **Add a README file**
3. Click **Create repository**

---

## Step 4 — Clone the Repository to Your Computer

Copy the repo URL from GitHub (green **Code** button → copy HTTPS URL)

```bash
git clone https://github.com/your-username/my-startup.git
cd my-startup
```

Now you have a local copy of the repo.

---

## Step 5 — Basic Git Workflow (Daily Use)

```
Edit files → Stage → Commit → Push
```

| Command | What it does |
|---------|-------------|
| `git status` | Show which files changed |
| `git add .` | Stage ALL changed files |
| `git add filename` | Stage one specific file |
| `git commit -m "message"` | Save a snapshot with a message |
| `git push` | Upload commits to GitHub |
| `git pull` | Download latest changes from GitHub |

**Example workflow:**
```bash
# After editing files...
git status                        # See what changed
git add .                         # Stage everything
git commit -m "Add homepage UI"   # Save snapshot
git push                          # Upload to GitHub
```

---

## Step 6 — Branching (Working in a Team)

> Never commit directly to `main` in a team project!

```bash
# Create and switch to a new branch
git checkout -b feature/login-page

# Work on your code...
git add .
git commit -m "Add login page"
git push origin feature/login-page
```

Then on GitHub → open a **Pull Request** → teammate reviews → **Merge** to main

---

## Recommended Folder Structure for a Startup Project

```
my-startup/
├── frontend/    ← Next.js project
├── backend/     ← Django project
└── README.md
```

---

## ✅ Checklist

- [ ] GitHub account created
- [ ] Git installed and configured
- [ ] Repository created on GitHub
- [ ] Repository cloned locally
- [ ] Practiced: add → commit → push
