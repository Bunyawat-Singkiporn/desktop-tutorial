# ⚡ Deploy Next.js Only — Vercel + Supabase (Free, No Backend Server)

**Stack:** Next.js (Vercel) + Supabase (PostgreSQL + Auth + API)

```
User's Browser
      │
      ▼
┌─────────────────┐          ┌──────────────────────┐
│     Vercel      │  direct  │      Supabase        │
│   (Next.js)     │─────────►│  PostgreSQL + Auth   │
│  Frontend + API │          │     + REST API       │
└─────────────────┘          └──────────────────────┘
```

> ใช้แนวทางนี้เมื่อ: ไม่ต้องการ Django, ต้องการ deploy ที่เดียว, ทีมถนัด JavaScript

---

## Part 1 — Set Up Supabase

### Step 1 — Create Supabase Project

1. Go to [https://supabase.com](https://supabase.com) → Login with GitHub
2. Click **New Project** → fill in name, password, region
3. Wait ~3 minutes

### Step 2 — Get API Keys

Go to **Settings → API**:

| Key | ใช้ทำอะไร |
|-----|---------|
| **Project URL** | Base URL สำหรับเรียก API |
| **anon public** | Key สำหรับเรียกจาก frontend (ปลอดภัยเมื่อใช้ RLS) |
| **service_role** | Key สำหรับ server-side เท่านั้น (ห้าม expose ใน browser) |

### Step 3 — Create a Table

1. Go to **Table Editor → New Table**
2. Example: สร้างตาราง `products`

| Column | Type | Default |
|--------|------|---------|
| `id` | int8 | auto |
| `name` | text | - |
| `price` | numeric | - |
| `created_at` | timestamptz | `now()` |

3. Click **Save**

---

## Part 2 — Set Up Next.js

### Step 4 — Install Supabase Client

```bash
cd frontend
npm install @supabase/supabase-js
```

### Step 5 — Set Up Environment Variables

Create `frontend/.env.local`:
```
NEXT_PUBLIC_SUPABASE_URL=https://xxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

Create `frontend/.env.example` (commit this):
```
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
```

### Step 6 — Create Supabase Client

Create `src/lib/supabase.js`:

```js
import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
);
```

### Step 7 — Fetch Data from Supabase

**Read data (Server Component):**

```jsx
// src/app/page.jsx
import { supabase } from "@/lib/supabase";

export default async function Home() {
  const { data: products } = await supabase
    .from("products")
    .select("*");

  return (
    <main>
      <h1>Products</h1>
      {products?.map((item) => (
        <p key={item.id}>{item.name} — {item.price}</p>
      ))}
    </main>
  );
}
```

**Insert data (Client Component):**

```jsx
// src/app/create/page.jsx
"use client";

import { useState } from "react";
import { supabase } from "@/lib/supabase";

export default function CreateProduct() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    const { error } = await supabase
      .from("products")
      .insert([{ name, price: Number(price) }]);

    if (!error) alert("Created!");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
      <input value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Price" />
      <button type="submit">Create</button>
    </form>
  );
}
```

### Step 8 — Push to GitHub

```bash
git add .
git commit -m "Setup Next.js with Supabase"
git push
```

---

## Part 3 — Deploy on Vercel

### Step 9 — Deploy to Vercel

1. Go to [https://vercel.com](https://vercel.com) → Login with GitHub
2. Click **New Project** → Import your repo
3. Set **Root Directory** to `frontend`
4. Click **Environment Variables** → Add:

| Key | Value |
|-----|-------|
| `NEXT_PUBLIC_SUPABASE_URL` | Your Supabase Project URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Your Supabase anon key |

5. Click **Deploy**

Your app is live at: `https://your-project.vercel.app`

---

## Supabase Built-in Features (Bonus)

Supabase ให้มากกว่าแค่ database:

| Feature | วิธีใช้ |
|---------|--------|
| **Auth** | `supabase.auth.signUp()`, `signInWithPassword()` |
| **Storage** | อัปโหลดไฟล์/รูปภาพ |
| **Realtime** | subscribe ดู data เปลี่ยนแบบ live |
| **Row Level Security** | กำหนดว่า user ไหนเข้าถึง row ไหนได้ |

---

## ⚠️ เมื่อไหร่ควรใช้แนวทางนี้ vs Django

| | **Next.js + Supabase** | **Next.js + Django + Supabase** |
|--|--|--|
| ทีม | JS เท่านั้น | มีคนถนัด Python |
| Logic ซับซ้อน | น้อย–ปานกลาง | มาก (custom business logic) |
| Deploy | Vercel เดียว | Vercel + Render |
| เวลา setup | เร็วกว่า | ช้ากว่า |
| เหมาะกับ | Hackathon, MVP | Production ใหญ่ |

---

## ✅ Checklist

- [ ] Supabase project created
- [ ] Table สร้างแล้ว
- [ ] API keys คัดลอกมาแล้ว
- [ ] `@supabase/supabase-js` installed
- [ ] `src/lib/supabase.js` สร้างแล้ว
- [ ] `.env.local` สร้างแล้ว (ไม่ commit)
- [ ] `.env.example` สร้างแล้ว (commit)
- [ ] ดึงข้อมูลจาก Supabase ได้
- [ ] Pushed to GitHub
- [ ] Deploy บน Vercel สำเร็จ
- [ ] Environment variables ตั้งค่าบน Vercel
- [ ] App ทำงานได้บน production ✅
