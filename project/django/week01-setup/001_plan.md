# Week 1 — Django Setup Sprint

> **ARCHIVE / REFERENCE ONLY** — Active path: [curriculum-48](../curriculum-48/000_overview.md)

## Goal Today
Get Django running with a live page **before leaving class** 🚀

## What is Django?

```
Browser  →  Django  →  HTML  →  Browser
(URL)       (Python)  (Page)   (You see it)
```

Django is a Python web framework — it turns Python code into web pages.

## Today's Plan

```
002_install.md   → Install Django
003_project.md   → Create project structure
004_firstpage.md → Write first view + run server
```

## What You'll Have by the End

```
http://127.0.0.1:8000/
```

A live webpage running on your computer. ✅

## Django vs Python Scripts

| Python script | Django |
|--------------|--------|
| You run it yourself | Browser triggers it |
| Prints to terminal | Returns HTML to browser |
| Runs once, stops | Keeps running, waits for requests |

## Files We'll Create Today

| File | What it does |
|------|-------------|
| `config/settings.py` | App configuration |
| `config/urls.py` | URL routing |
| `board/views.py` | Page logic |
| `board/urls.py` | App URLs |
