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

## Step 2 — Project Structure

```
frontend/
├── src/
│   └── app/
│       ├── page.jsx        ← Home page  (localhost:3000/)
│       ├── layout.jsx      ← Shared layout (navbar, footer)
│       ├── globals.css     ← Global styles
│       └── about/
│           └── page.jsx    ← About page (localhost:3000/about)
├── public/                 ← Static files (images, icons)
├── package.json            ← Project dependencies
└── next.config.js          ← Next.js configuration
```

> 📌 **Routing rule:** Each folder inside `app/` with a `page.jsx` file becomes a URL path automatically.

---

## Step 3 — Run the Development Server

```bash
cd frontend
npm run dev
```

Open your browser: [http://localhost:3000](http://localhost:3000)

You should see the default Next.js welcome page.

---

## Step 4 — Edit Your First Page

Open `src/app/page.jsx` and replace the content:

```jsx
export default function Home() {
  return (
    <main>
      <h1>Welcome to My Startup 🚀</h1>
      <p>We are building something awesome.</p>
    </main>
  );
}
```

Save the file — the browser **updates automatically** (Hot Reload).

---

## Step 5 — Create a New Page

Create a new folder and file: `src/app/about/page.jsx`

```jsx
export default function About() {
  return (
    <main>
      <h1>About Us</h1>
      <p>Our mission is to solve real problems.</p>
    </main>
  );
}
```

Visit [http://localhost:3000/about](http://localhost:3000/about) — the page appears automatically!

---

## Step 6 — Add a Navbar (Shared Layout)

Open `src/app/layout.jsx` and add a simple nav:

```jsx
import "./globals.css";

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <nav>
          <a href="/">Home</a> |{" "}
          <a href="/about">About</a>
        </nav>
        {children}
      </body>
    </html>
  );
}
```

The navbar now appears on **every page** automatically.

---

## Step 7 — Set Up Environment Variables

Create `frontend/.env.local` **(do this before writing any fetch calls)**:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

> `NEXT_PUBLIC_` prefix makes the variable available in the browser.
> ⚠️ Add `.env.local` to `.gitignore` — never commit this file!

Check that `.gitignore` inside `frontend/` already contains (it should by default):
```
.env.local
```

---

## Step 8 — Connect to Django Backend

Next.js sends HTTP requests to Django. There are two patterns:

### Pattern A — GET (read data)

Used on **Server Components** (default in App Router). Runs on the server.

```jsx
// src/app/page.jsx

async function getProducts() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/products/`);
  return res.json();
}

export default async function Home() {
  const products = await getProducts();
  return (
    <main>
      <h1>Products</h1>
      {products.map((item) => (
        <div key={item.id}>
          <h2>{item.name}</h2>
          <p>{item.description}</p>
          <p>Price: {item.price}</p>
        </div>
      ))}
    </main>
  );
}
```

---

### Pattern B — POST (send data)

Used in **forms or buttons** inside Client Components.

```jsx
// src/app/create/page.jsx
"use client";  // ← needed for useState and event handlers

import { useState } from "react";

export default function CreateProduct() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/products/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: name, price: price, description: "" }),
    });

    if (res.ok) {
      alert("Product created!");
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Product name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      <button type="submit">Create</button>
    </form>
  );
}
```

---

## Summary — Server vs Client Component

| | Server Component | Client Component |
|---|---|---|
| **Default?** | Yes | Add `"use client"` at top |
| **Can fetch on load?** | ✅ Yes | ✅ Yes (use `useEffect`) |
| **Can use useState?** | ❌ No | ✅ Yes |
| **Use for** | Displaying data | Forms, buttons, interactions |

---

## Step 9 — Push to GitHub

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
- [ ] Home page edited successfully
- [ ] New page created (about/)
- [ ] Navbar added in layout
- [ ] `.env.local` created with `NEXT_PUBLIC_API_URL=http://localhost:8000`
- [ ] GET request to Django working (products list)
- [ ] POST request to Django working (create form)
- [ ] Pushed to GitHub
