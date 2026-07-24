# Django Backend Practice — 48 Sessions

## Who this is for

Adults / bootcamp learners who have touched Django before but forgot the basics — especially **API, server, ERD, and database**.

## Stack

| Layer | Tech |
|-------|------|
| Backend | Django + Django REST Framework (DRF) + SQLite (class) |
| Frontend | React (Vite) + Tailwind + `fetch` |
| Auth (from Block D) | JWT (SimpleJWT) |
| Ports | Backend `:8000` · Frontend `:5173` |

## Class rules (golden)

1. Draw **ERD** or **request/response** before coding (especially early blocks).
2. Test API with browser / Thunder Client / curl **before** wiring React.
3. **One React page ≈ one API lesson** (login page, table page, etc.).
4. Always run **both** servers: `backend/` + `frontend/`.

## Teaching pattern

```
Concept (ERD / HTTP) → Model → DRF API → React page → Demo both servers
```

## Folder layout

```
curriculum-48/
  000_overview.md          ← you are here
  README.md
  sessions/                ← S01 … S48 lesson sheets
  starter/                 ← copy this to start a new project
    backend/
    frontend/
  projects/                ← student / class project homes
    p01-taskboard/
    p02-auth-app/
    p03-minishop/
    p04-capstone/
```

## Curriculum map

### Block A — Foundations (S01–S08)

Reset mental model: web, HTTP, API, DB, ERD, Django refresh.

| Session | Focus |
|---------|--------|
| [S01](sessions/S01_web_request_response.md) | Browser, server, request/response |
| [S02](sessions/S02_http_json.md) | Method, status, headers, JSON |
| [S03](sessions/S03_what_is_api.md) | API vs HTML page; call a public API |
| [S04](sessions/S04_database_basics.md) | Table, row, PK, FK |
| [S05](sessions/S05_erd_shop.md) | ERD by hand: 1:1, 1:N, N:M |
| [S06](sessions/S06_sql_basics.md) | SELECT / INSERT / UPDATE / DELETE |
| [S07](sessions/S07_django_refresh.md) | Project/app, settings, runserver, urls |
| [S08](sessions/S08_model_admin.md) | Model + migrate + Admin |

**Deliverable:** one ERD + one Model visible in Admin

### Block B — API + React glue (S09–S16)

| Session | Focus |
|---------|--------|
| [S09](sessions/S09_drf_list.md) | Serializer + List API |
| [S10](sessions/S10_detail_create.md) | Detail + Create |
| [S11](sessions/S11_update_delete.md) | Update + Delete |
| [S12](sessions/S12_cors_react_setup.md) | CORS + Vite React + Tailwind |
| [S13](sessions/S13_react_table.md) | `fetch` list → table page |
| [S14](sessions/S14_react_create.md) | Create form → POST |
| [S15](sessions/S15_react_edit_delete.md) | Edit / Delete from table |
| [S16](sessions/S16_error_handling.md) | 400/401/404 on UI |

**Deliverable:** mini Task CRUD (API + React)

### Block C — Project 1: Task Board (S17–S24)

Multi-page app; each page uses a different API shape.

| Session | Page / topic | API skill |
|---------|--------------|-----------|
| [S17](sessions/S17_dashboard_stats.md) | Dashboard | aggregate counts |
| [S18](sessions/S18_tasks_filter.md) | Tasks table | `?status=` |
| [S19](sessions/S19_task_detail_notes.md) | Task detail | nested / related |
| [S20](sessions/S20_search_pagination.md) | Search | search, ordering, pagination |
| [S21](sessions/S21_categories_fk.md) | Categories | FK + second API |
| [S22](sessions/S22_validation.md) | Validation | unique, blank/null |
| [S23](sessions/S23_ux_loading.md) | UX | loading / empty / toast |
| [S24](sessions/S24_project1_review.md) | Review | polish Project 1 |

### Block D — Project 2: Auth + Me (S25–S32)

| Session | Focus |
|---------|--------|
| [S25](sessions/S25_auth_concepts.md) | Session vs token vs JWT |
| [S26](sessions/S26_register.md) | Register API + page |
| [S27](sessions/S27_login_token.md) | Login + store token |
| [S28](sessions/S28_protected_routes.md) | Protected routes + header |
| [S29](sessions/S29_me_profile.md) | `/api/me/` |
| [S30](sessions/S30_password_logout.md) | Change password / logout |
| [S31](sessions/S31_ownership.md) | User sees only own data |
| [S32](sessions/S32_auth_review.md) | Lock Task CRUD behind auth |

### Block E — Project 3: Mini Shop (S33–S40)

| Session | Focus |
|---------|--------|
| [S33](sessions/S33_shop_erd.md) | ERD: Product, Category, Order |
| [S34](sessions/S34_products_table.md) | Products table + filter |
| [S35](sessions/S35_product_form.md) | Create/edit + FK id |
| [S36](sessions/S36_orders_list.md) | Orders + join-style fields |
| [S37](sessions/S37_order_create.md) | Create order + line items |
| [S38](sessions/S38_stock_rules.md) | Stock business rules |
| [S39](sessions/S39_permissions.md) | Staff vs normal user |
| [S40](sessions/S40_shop_review.md) | End-to-end demo |

### Block F — Capstone light (S41–S48)

Not a timed hackathon — pick **one** theme (Blog / Helpdesk / Classroom) and build page by page.

| Session | Focus |
|---------|--------|
| [S41](sessions/S41_capstone_plan.md) | Theme + ERD + page/API list |
| [S42](sessions/S42_capstone_models.md) | Models + seed data |
| [S43](sessions/S43_capstone_auth_layout.md) | Auth + main layout |
| [S44](sessions/S44_capstone_table.md) | Main table + pagination |
| [S45](sessions/S45_capstone_detail.md) | Detail + related |
| [S46](sessions/S46_capstone_forms.md) | Forms + validation |
| [S47](sessions/S47_deploy_checklist.md) | Env / production-like checklist |
| [S48](sessions/S48_demo_day.md) | Demo day + full checklist |

## Session sheet format

Every `sessions/Sxx_*.md` uses:

```
# Sxx — Title
## Goal
## Concept (5 min)
## Backend steps
## Frontend steps
## Check
## Common bugs
```

## Defaults

- Main path = **API + React**, not Django Templates
- Auth from Block D = **JWT (SimpleJWT)**
- DB in class = **SQLite**; PostgreSQL mentioned in S47
- [project1-noticeboard](../project1-noticeboard/) and hackathon = **archive / cancelled**

## How to start class

1. Copy [starter/](starter/) → `projects/p01-taskboard/` (or next project)
2. Open today’s sheet under `sessions/`
3. Run backend + frontend and follow Goal → Check
