# Quick Start — Before You Begin

---

## Assumptions

This guide assumes:
- ✅ You have a GitHub account
- ✅ Git is installed on your computer
- ✅ You have a GitHub repository created (e.g. `my-startup`)
- ✅ You've cloned it locally and are ready to code

```bash
git clone https://github.com/your-username/my-startup.git
cd my-startup
```

---

## Project Structure

Create this folder structure:

```
my-startup/
├── frontend/    ← Next.js app (Steps 025)
├── backend/     ← Django app (Steps 026)
└── README.md
```

---

## Tools You Need

Install these before starting:

| Tool | Download | Check |
|------|----------|-------|
| **Node.js** (v18+) | [nodejs.org](https://nodejs.org) | `node --version` |
| **Python** (3.10+) | [python.org](https://python.org) | `python --version` |
| **Git** | [git-scm.com](https://git-scm.com) | `git --version` |

---

## Basic Git Workflow

After making changes, upload to GitHub:

```bash
git add .
git commit -m "Add feature description"
git push
```

For team projects, use branches:
```bash
git checkout -b feature/feature-name
# ... make changes ...
git push origin feature/feature-name
# Then open a Pull Request on GitHub
```

---

## ✅ Checklist Before Starting

- [ ] GitHub repo cloned locally
- [ ] Node.js (v18+) installed
- [ ] Python (3.10+) installed
- [ ] Create `frontend/` folder
- [ ] Create `backend/` folder
- [ ] Ready for Step 025 (Next.js)
