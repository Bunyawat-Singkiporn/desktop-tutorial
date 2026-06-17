# ⚡ Next.js Frontend Setup — Step by Step

---

## What is Next.js?

**Next.js** is a React framework that makes it easy to build fast, modern web apps.

| Feature | Benefit |
|---------|---------|
| File-based routing | No need to configure routes manually |
| Server-side rendering | Faster page load, better SEO |
| Easy Deployment | Designed to deploy on Vercel in 1 click |
| Works with any backend | Sends requests to Django API — no backend code needed in Next.js |

> 📌 In this class, **Next.js is only the frontend**. All data comes from the **Django backend**. We do NOT use Next.js API Routes.

---

## Prerequisites

**Install Node.js** (includes `npm`)

1. Go to [https://nodejs.org](https://nodejs.org)
2. Download the **LTS** version
3. Run the installer

**Verify installation:**
```bash
node --version    # should show v18 or higher
npm --version
```

---

## Step 1 — Create a Next.js Project

Go to your project folder first:
```bash
cd my-startup
```

Create the Next.js app inside a `frontend` folder:
```bash
npx create-next-app@latest frontend
```

**Answer the prompts:**
```
✔ Would you like to use TypeScript?              → No
✔ Would you like to use ESLint?                  → Yes
✔ Would you like to use Tailwind CSS?            → Yes
✔ Would you like to use `src/` directory?        → Yes
✔ Would you like to use App Router?              → Yes
✔ Would you like to customize the import alias?  → No
```

---

## Step 2 — Best Practice Folder Structure

After creating the project, **reorganize `src/` to follow this structure**:

```
frontend/
├── src/
│   ├── app/                        ← Pages & routing (Next.js App Router)
│   │   ├── (auth)/                 ← Route group (no URL prefix)
│   │   │   ├── login/
│   │   │   │   └── page.jsx
│   │   │   └── register/
│   │   │       └── page.jsx
│   │   ├── products/
│   │   │   ├── page.jsx            ← /products
│   │   │   └── [id]/
│   │   │       └── page.jsx        ← /products/1
│   │   ├── layout.jsx              ← Root layout (navbar, footer)
│   │   ├── page.jsx                ← Home page /
│   │   └── globals.css
│   ├── components/                 ← Reusable UI pieces
│   │   ├── ui/                     ← Generic: Button, Input, Card
│   │   │   ├── Button.jsx
│   │   │   └── Card.jsx
│   │   └── layout/                 ← Structural: Navbar, Footer, Sidebar
│   │       ├── Navbar.jsx
│   │       └── Footer.jsx
│   ├── lib/                        ← Utility functions & API calls
│   │   ├── api.js                  ← All fetch() calls to Django in one place
│   │   └── utils.js                ← Helpers (format date, format price)
│   └── hooks/                      ← Custom React hooks (Client Components)
│       └── useProducts.js          ← e.g. fetch + loading + error state
├── public/                         ← Static files (images, icons, fonts)
├── .env.local                      ← Local env vars (never commit!)
├── .env.example                    ← Template showing what vars are needed
├── .gitignore
├── next.config.js
└── package.json
```

### Key folders explained

| Folder | What goes here |
|--------|----------------|
| `app/` | Pages only — one `page.jsx` per route |
| `components/ui/` | Small reusable pieces: Button, Card, Badge |
| `components/layout/` | Structural pieces: Navbar, Footer, Sidebar |
| `lib/api.js` | **All** `fetch()` calls to Django — never call fetch directly in pages |
| `lib/utils.js` | Pure helper functions (no React) |
| `hooks/` | Custom hooks that wrap `useState`/`useEffect` |

### `lib/api.js` example

Centralize all API calls here so pages stay clean:

```js
// src/lib/api.js
const BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getProducts() {
  const res = await fetch(`${BASE_URL}/api/products/`);
  if (!res.ok) throw new Error("Failed to fetch products");
  return res.json();
}

export async function createProduct(data) {
  const res = await fetch(`${BASE_URL}/api/products/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create product");
  return res.json();
}

export async function deleteProduct(id) {
  const res = await fetch(`${BASE_URL}/api/products/${id}/`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete product");
}
```

Then in your page, just import and call:

```jsx
// src/app/products/page.jsx
import { getProducts } from "@/lib/api";

export default async function ProductsPage() {
  const products = await getProducts();
  return (
    <main>
      {products.map((p) => <p key={p.id}>{p.name}</p>)}
    </main>
  );
}
```

### `.env.example` — commit this file!

Create `frontend/.env.example` (safe to commit, no real values):
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

> When a teammate clones the repo, they copy this file to `.env.local` and fill in the values.

---

## Step 3 — Run the Development Server

```bash
cd frontend
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) — you should see the Next.js welcome page.

---

## Step 4 — Set Up Environment Variables

Create `frontend/.env.local` **(do this before writing any fetch calls)**:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

> `NEXT_PUBLIC_` prefix makes the variable available in the browser.
> ⚠️ Add `.env.local` to `.gitignore` — this file should **never** be committed.

Create `frontend/.env.example` (safe to commit):
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Step 5 — Connect to Django Backend & Start Coding

Edit `src/app/page.jsx` to fetch from Django:

```jsx
// Server Component (default) — fetches on the server
async function getProducts() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/products/`);
  return res.json();
}

export default async function Home() {
  const products = await getProducts();
  return (
    <main>
      <h1>Products</h1>
      {products?.map((item) => (
        <p key={item.id}>{item.name}</p>
      ))}
    </main>
  );
}
```

For forms (sends data to Django), use `"use client"`:

```jsx
"use client";

import { useState } from "react";

export default function CreateProduct() {
  const [name, setName] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/products/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, description: "", price: 0 }),
    });
    if (res.ok) alert("Created!");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button type="submit">Create</button>
    </form>
  );
}
```

**Server vs Client Components:**
- **Server Component** (default): Best for fetching data on page load
- **Client Component** (`"use client"`): Required for forms, buttons, `useState`

---

## Step 6 — Push to GitHub

```bash
cd ..             # go back to my-startup root
git add .
git commit -m "Add Next.js frontend"
git push
```

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run start` | Run production build locally |
| `npm install package-name` | Install a new package |

---

## ✅ Checklist

- [ ] Node.js installed (v18+)
- [ ] Next.js project created in `frontend/`
- [ ] Dev server running on localhost:3000
- [ ] `.env.local` created with `NEXT_PUBLIC_API_URL=http://localhost:8000`
- [ ] `.env.example` created (committed to GitHub)
- [ ] Fetching data from Django working
- [ ] Pushed to GitHub
