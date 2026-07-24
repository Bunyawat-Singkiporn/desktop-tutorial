# Generates S01–S48 lesson sheets. Run once from repo.
from pathlib import Path

BASE = Path(__file__).resolve().parent / "sessions"
BASE.mkdir(parents=True, exist_ok=True)


def write(name, title, goal, concept, backend, frontend, check, bugs):
    be = "\n".join(f"- {x}" for x in backend)
    fe = "\n".join(f"- {x}" for x in frontend)
    ch = "\n".join(f"- [ ] {x}" for x in check)
    bu = "\n".join(f"- {x}" for x in bugs)
    text = f"""# {title}

## Goal

{goal}

## Concept (5 min)

{concept}

## Backend steps

{be}

## Frontend steps

{fe}

## Check

{ch}

## Common bugs

{bu}
"""
    (BASE / name).write_text(text, encoding="utf-8")


# --- Block A ---
write(
    "S01_web_request_response.md",
    "S01 — Web: Browser, Server, Request/Response",
    "Explain how a browser talks to a server and what comes back.",
    "A website is a conversation:\n1. Browser sends a **request**\n2. Server runs code / reads DB\n3. Server sends a **response** (HTML, JSON, or error).\n\nDjango lives on the **server**, not in the browser.",
    [
        "Draw: Browser -> Server -> Response on paper",
        "Label: URL, method, body, status",
    ],
    ["No code today — discussion + drawing only"],
    [
        "Can explain request vs response in one sentence",
        "Can point to where Django will sit later (the server)",
    ],
    ['Thinking the browser "runs Python" — it does not'],
)

write(
    "S02_http_json.md",
    "S02 — HTTP: Method, Status, Headers, JSON",
    "Read an HTTP exchange and recognize method, status, and JSON body.",
    "**Methods:** GET (read), POST (create), PUT/PATCH (update), DELETE\n"
    "**Status:** 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Server Error\n"
    '**JSON:** data format APIs use — `{ "name": "Ada" }`',
    [
        "Open DevTools -> Network; click one request",
        "Write down: method, status, Content-Type",
    ],
    ["Paste sample JSON and identify keys/values"],
    [
        "List 4 methods and what they mean",
        "Match status codes 200 / 400 / 401 / 404",
    ],
    ["Confusing PUT vs PATCH — PATCH = partial update"],
)

write(
    "S03_what_is_api.md",
    "S03 — What is an API (vs HTML page)",
    "Call a public API and contrast an HTML page vs a JSON API.",
    "HTML page = for humans in the browser.\n"
    "API = for programs to exchange data (usually JSON).\n"
    "Same server can serve both; this course focuses on JSON APIs.",
    [
        "GET a public API (e.g. https://jsonplaceholder.typicode.com/todos/1)",
        "Compare viewing a website vs viewing raw JSON",
    ],
    ["Sketch future app pages and which data each needs from an API"],
    [
        "Explain API vs web page to a partner",
        "Show one successful GET with a JSON body",
    ],
    ["Expecting HTML from an API URL — check Content-Type"],
)

write(
    "S04_database_basics.md",
    "S04 — Database: Table, Row, PK, FK",
    "Name the building blocks of a relational database.",
    "**Table** = one entity (User, Task)\n"
    "**Row** = one record\n"
    "**Column** = one field\n"
    "**PK** = unique id of a row\n"
    "**FK** = points to another table's PK",
    [
        "Given a shop scenario, list 2–3 tables and columns",
        "Mark which column is PK",
    ],
    ["No Django yet — paper / whiteboard"],
    [
        "Define PK and FK in your own words",
        "Draw one FK arrow between two tables",
    ],
    ["Using name as PK — prefer an auto id"],
)

write(
    "S05_erd_shop.md",
    "S05 — ERD by hand (Shop: 1:1, 1:N, N:M)",
    "Draw an ERD for a mini shop with correct relationship types.",
    "**1:1** — User <-> Profile\n"
    "**1:N** — Category -> many Products\n"
    "**N:M** — Order <-> Product (via OrderLine join table)",
    [
        "Entities: Category, Product, Order, OrderLine, Customer",
        "Draw boxes + lines; label 1:N / N:M",
    ],
    ["Optional: redraw the same ERD in draw.io"],
    [
        "ERD shows at least one 1:N and one N:M (with join table)",
        "Every box has a PK",
    ],
    ["Drawing N:M without a join table"],
)

write(
    "S06_sql_basics.md",
    "S06 — SQL basics: SELECT / INSERT / UPDATE / DELETE",
    "Write and understand the four CRUD SQL statements.",
    "Create -> INSERT\nRead -> SELECT\nUpdate -> UPDATE\nDelete -> DELETE\n\n"
    "Django Models hide SQL, but SQL still runs underneath.",
    [
        "Write all four statements for a `tasks(id, title, done)` table on paper",
        "Optional: run them in DB Browser for SQLite",
    ],
    ["Map each SQL verb to a future API method (GET/POST/PATCH/DELETE)"],
    [
        "Correct examples of all four verbs",
        "Know UPDATE/DELETE without WHERE is dangerous",
    ],
    ["Forgetting WHERE on UPDATE/DELETE"],
)

write(
    "S07_django_refresh.md",
    "S07 — Django refresh: project, app, settings, urls, runserver",
    "Create/run a Django project and hit a hello URL.",
    "**Project** = whole site (settings, root urls)\n"
    "**App** = one feature module\n"
    "`runserver` = local development server",
    [
        "Use course starter or: django-admin startproject config .",
        "python manage.py startapp core",
        "Wire urls -> simple view returning HttpResponse or JsonResponse",
        "python manage.py runserver",
    ],
    ["Visit http://127.0.0.1:8000/ and confirm response"],
    ["Server runs without error", "Can explain project vs app"],
    ["Wrong venv / Django not installed", "Editing the wrong urls.py"],
)

write(
    "S08_model_admin.md",
    "S08 — Model + migrate + Admin (ERD -> Model)",
    "Turn one ERD entity into a Model and manage it in Admin.",
    "Model = Python class that becomes a DB table.\n"
    "makemigrations = plan changes\n"
    "migrate = apply changes\n"
    "Admin = built-in UI for data entry",
    [
        "Create model matching ERD (e.g. Task: title, done, created_at)",
        "makemigrations + migrate",
        "Register in admin; createsuperuser",
        "Add 3 rows in Admin",
    ],
    ["No React yet — Admin is enough for data"],
    ["Model appears in Admin", "DB updated after migrate"],
    ["Forgot migrate", "Forgot to register the model in admin.py"],
)

# --- Block B ---
write(
    "S09_drf_list.md",
    "S09 — DRF: Serializer + List API (GET /api/items/)",
    "Expose a list of model rows as JSON via DRF.",
    "Serializer = Model <-> JSON.\n"
    "List API = GET collection endpoint.\n"
    "Prefer ViewSet or ListAPIView for class.",
    [
        "pip install djangorestframework (if not in starter)",
        "Add rest_framework to INSTALLED_APPS",
        "Serializer for Task",
        "GET /api/tasks/ returns JSON array",
    ],
    ["Open /api/tasks/ in browser or Thunder Client"],
    ["JSON list matches Admin data", "Status 200"],
    ["Forgot DEFAULT permissions blocking browse", "Circular import in urls"],
)

write(
    "S10_detail_create.md",
    "S10 — Detail + Create (GET one / POST)",
    "Add retrieve-one and create endpoints.",
    "GET /api/tasks/1/ = one object\n"
    "POST /api/tasks/ = create with JSON body\n"
    "201 Created on success",
    [
        "Add retrieve route by pk",
        "Add create; validate title required",
        "Test POST with Thunder Client",
    ],
    ["Still no React — API client only"],
    ["GET detail works", "POST creates row visible in Admin"],
    ["Sending form-urlencoded instead of JSON", "Missing CSRF on session auth — use Token/JWT or AllowAny for now"],
)

write(
    "S11_update_delete.md",
    "S11 — Update + Delete (PUT/PATCH/DELETE)",
    "Finish CRUD on the Task API.",
    "PUT = replace whole object\n"
    "PATCH = partial update\n"
    "DELETE = remove row (204 or 204/200)",
    [
        "PATCH /api/tasks/1/ { \"done\": true }",
        "DELETE /api/tasks/1/",
        "Confirm in Admin",
    ],
    ["Document the five endpoints on paper"],
    ["All five verbs work on tasks", "Wrong id returns 404"],
    ["Using PUT when only one field changes — prefer PATCH"],
)

write(
    "S12_cors_react_setup.md",
    "S12 — CORS + React Vite + Tailwind first run",
    "Run React frontend alongside Django and fix CORS.",
    "Browsers block cross-origin API calls unless the server allows them.\n"
    "django-cors-headers + CORS_ALLOWED_ORIGINS for http://localhost:5173",
    [
        "Install/enable django-cors-headers",
        "Allow http://localhost:5173",
        "Confirm /api/tasks/ still works",
    ],
    [
        "Use course starter/frontend or: npm create vite@latest",
        "Add Tailwind per Vite guide",
        "npm run dev on :5173",
        "Show a Hello page",
    ],
    ["Both servers running", "No CORS error in console for a test fetch"],
    ["Typo in CORS origin", "Calling http vs https mismatch"],
)

write(
    "S13_react_table.md",
    "S13 — fetch list -> simple table page",
    "Build a Tasks table page that loads from GET /api/tasks/.",
    "useEffect + fetch on mount.\n"
    "Map JSON array to <table> or Tailwind rows.",
    ["Ensure list endpoint AllowAny or provide token later"],
    [
        "Create TasksPage",
        "fetch(`${API}/api/tasks/`)",
        "Render title + done columns",
        "Route /tasks",
    ],
    ["Table shows same rows as Admin", "Loading state optional"],
    ["Forgetting await / .json()", "Hardcoding wrong API base URL"],
)

write(
    "S14_react_create.md",
    "S14 — Create form from React -> POST API",
    "Add a form that POSTs a new task and refreshes the list.",
    "POST with Content-Type: application/json\n"
    'Body: { "title": "..." }',
    ["Confirm POST still works in Thunder Client"],
    [
        "Controlled input + submit handler",
        "POST then refetch list or append",
        "Clear input on success",
    ],
    ["New task appears without refreshing Admin only", "Empty title shows validation feedback"],
    ["Not stringifying body", "Missing headers"],
)

write(
    "S15_react_edit_delete.md",
    "S15 — Edit / Delete from the table",
    "Toggle done with PATCH and remove with DELETE from the UI.",
    "Each row action calls a different method on the same resource URL.",
    ["PATCH and DELETE verified in API client"],
    [
        "Toggle done checkbox -> PATCH",
        "Delete button -> DELETE + confirm",
        "Update local state or refetch",
    ],
    ["Toggle and delete work end-to-end"],
    ["Updating wrong id", "UI state out of sync with server"],
)

write(
    "S16_error_handling.md",
    "S16 — Error handling: 400 / 401 / 404 on UI",
    "Show user-friendly errors when the API fails.",
    "Read response.ok; parse error JSON from DRF.\n"
    "Map status to message: 400 validation, 401 login, 404 missing.",
    ["Force a 400 (empty title) and note response body shape"],
    [
        "Centralize apiFetch helper in src/api/client.js",
        "Show banner / toast on error",
        "Disable double-submit while loading",
    ],
    ["Bad POST shows message, not silent fail", "Network error handled"],
    ["Assuming error body is always a string"],
)

# --- Block C ---
write(
    "S17_dashboard_stats.md",
    "S17 — Dashboard page: aggregate stats API",
    "Build a dashboard that shows counts from a stats endpoint.",
    "Not every page is a table — dashboards need aggregates.\n"
    "Example: GET /api/tasks/stats/ -> { total, done, todo }",
    [
        "Add stats action on ViewSet or separate view",
        "Use Count / filter in queryset",
    ],
    [
        "Dashboard page with 3 cards: Total / Done / Todo",
        "fetch stats on load",
    ],
    ["Numbers match reality in Admin"],
    ["Heavy client-side counting when server can aggregate"],
)

write(
    "S18_tasks_filter.md",
    "S18 — Tasks table with ?status= filter",
    "Filter list with query params.",
    "GET /api/tasks/?status=todo\n"
    "Query params are part of the URL, not the body.",
    [
        "Filter queryset by request.GET.get('status')",
        "Document allowed values",
    ],
    [
        "Filter buttons or select on Tasks page",
        "Change URL search params and refetch",
    ],
    ["Filter todo/done works", "Clear filter shows all"],
    ["Forgetting to reset page when combining with pagination later"],
)

write(
    "S19_task_detail_notes.md",
    "S19 — Task detail with related notes",
    "Show one task and nested related notes.",
    "1:N Task -> Notes\n"
    "Serializer can nest NoteSerializer(many=True, read_only=True)",
    [
        "Note model with FK to Task",
        "Nested serializer on detail",
        "Optional: POST /api/tasks/1/notes/",
    ],
    [
        "Detail route /tasks/:id",
        "Render task fields + notes list",
    ],
    ["Detail shows nested notes", "404 for missing id"],
    ["N+1 queries — ok for class size; mention select_related later"],
)

write(
    "S20_search_pagination.md",
    "S20 — Search, ordering, pagination",
    "Add search + ordering + page size to the list API and UI.",
    "DRF: SearchFilter, OrderingFilter, PageNumberPagination\n"
    "Frontend: search box + next/prev",
    [
        "Configure filter_backends and pagination_class",
        "Test ?search=&ordering=&page=",
    ],
    [
        "Search input debounced or on submit",
        "Prev/Next using page links from response",
    ],
    ["Search finds by title", "Page 2 works when enough rows"],
    ["Ignoring paginated response shape { count, results }"],
)

write(
    "S21_categories_fk.md",
    "S21 — Categories FK + dropdown from second API",
    "Assign each task a category from a separate list endpoint.",
    "FK in JSON is often just category: <id>\n"
    "UI loads /api/categories/ for a select dropdown.",
    [
        "Category model; Task.category FK",
        "Category list API",
        "Accept category id on Task write",
    ],
    [
        "Load categories into <select>",
        "Show category name on table (serializer field category_name)",
    ],
    ["Create task with category works", "Null category handled"],
    ["Sending category name instead of id"],
)

write(
    "S22_validation.md",
    "S22 — Validation: unique, blank/null",
    "Make the API reject bad data with clear errors.",
    "Model constraints vs Serializer.validate_\n"
    "unique=True, blank vs null for strings/FKs",
    [
        "Unique title (or unique per user later)",
        "Custom validate_title",
        "Return 400 with field errors",
    ],
    ["Show field errors under inputs"],
    ["Duplicate title returns 400", "UI shows which field failed"],
    ["null=True without blank=True surprises for CharField"],
)

write(
    "S23_ux_loading.md",
    "S23 — UX: loading, empty, toast",
    "Polish Task Board UX states.",
    "Loading spinner while fetching\n"
    "Empty state when results=[]\n"
    "Toast on success/error",
    ["No backend change required unless adding message fields"],
    [
        "isLoading / isEmpty flags",
        "Simple toast component",
        "Disable buttons while mutating",
    ],
    ["Empty list does not look broken", "Success feedback on create"],
    ["Infinite loading if fetch never settles — check errors"],
)

write(
    "S24_project1_review.md",
    "S24 — Review + polish Project 1 (Task Board)",
    "Demo Task Board end-to-end and fix gaps.",
    "Checklist day: multi-page app with different APIs per page.",
    [
        "Verify stats, filter, detail+notes, search, categories, validation",
        "Clean dead code / print statements",
    ],
    [
        "Walk all pages in nav",
        "Fix UX bugs found in demo",
    ],
    [
        "Dashboard + table + detail all work",
        "Partner can use the app without coaching",
    ],
    ["Half-working pages left for 'later' — close or ticket them"],
)

# --- Block D ---
write(
    "S25_auth_concepts.md",
    "S25 — Auth concepts: session vs token vs JWT",
    "Choose JWT for this course and know why.",
    "**Session:** cookie on browser; server stores session\n"
    "**Token:** key in Authorization header\n"
    "**JWT:** signed token; access (+ refresh) pattern with SimpleJWT",
    [
        "Discuss which fits SPA (React) best — JWT/token",
        "Install djangorestframework-simplejwt (starter may include)",
    ],
    ["No UI yet — whiteboard auth flow"],
    ["Can explain why SPA often uses JWT", "Draw login -> token -> Authorization header"],
    ["Storing JWT in localStorage vs httpOnly cookie tradeoffs — mention only"],
)

write(
    "S26_register.md",
    "S26 — Register API + Register page",
    "Create a user via API and a Register form in React.",
    "POST /api/auth/register/ { username, password }\n"
    "Never return password hashes to client",
    [
        "Register serializer + view",
        "Create User; return 201 + public fields",
    ],
    [
        "Register page",
        "On success navigate to login",
    ],
    ["New user appears in Admin", "Weak/empty password rejected"],
    ["Returning password in response"],
)

write(
    "S27_login_token.md",
    "S27 — Login API + store token",
    "Login and store access token for later requests.",
    "POST /api/auth/token/ (SimpleJWT) -> access, refresh\n"
    "Save access token (localStorage for class simplicity)",
    [
        "Wire SimpleJWT urls",
        "Test token obtain in Thunder Client",
    ],
    [
        "Login page",
        "Save token; redirect to app home",
    ],
    ["Token returned and stored", "Bad credentials show error"],
    ["Calling protected API without Bearer prefix"],
)

write(
    "S28_protected_routes.md",
    "S28 — Protected routes + Authorization header",
    "Block React routes and API calls without a token.",
    "DRF: IsAuthenticated\n"
    "React: wrapper route checking token\n"
    "api client attaches Authorization: Bearer <access>",
    [
        "Set default permission IsAuthenticated on task APIs",
        "Confirm 401 without token",
    ],
    [
        "Auth header in client.js",
        "Redirect to /login when missing token",
    ],
    ["With token: 200", "Without: 401 + redirect"],
    ["Expired token — mention refresh endpoint exists"],
)

write(
    "S29_me_profile.md",
    "S29 — /api/me/ profile page",
    "Show the current user from the access token.",
    "GET /api/me/ uses request.user\n"
    "No user id in URL — identity comes from token",
    [
        "Me view returning id, username, email",
    ],
    [
        "Profile page fetching /api/me/",
        "Show username in navbar",
    ],
    ["Correct user shown after login"],
    ["Trusting user id from query string instead of request.user"],
)

write(
    "S30_password_logout.md",
    "S30 — Change password / logout",
    "Change password via API; logout on the client.",
    "Logout with JWT = delete token client-side (and optional blacklist refresh).\n"
    "Change password: verify old password first.",
    [
        "Change-password endpoint",
        "Optional: refresh token blacklist",
    ],
    [
        "Logout clears token + redirect",
        "Change password form",
    ],
    ["Logout prevents further API calls", "Password change works then re-login"],
    ["Only clearing UI state but leaving token"],
)

write(
    "S31_ownership.md",
    "S31 — Ownership: user sees only own data",
    "Filter querysets so users cannot read/write others' tasks.",
    "task.owner = request.user on create\n"
    "get_queryset filters owner=request.user\n"
    "Object-level check on update/delete",
    [
        "Add owner FK to Task",
        "Perform_create set owner",
        "Filter queryset",
    ],
    ["Two users: A cannot see B's tasks"],
    ["Isolation verified with two accounts"],
    ["Forgot filter on detail — IDOR risk"],
)

write(
    "S32_auth_review.md",
    "S32 — Auth review: lock Task CRUD behind auth",
    "Integrate Auth project with Task Board and demo.",
    "Register -> Login -> Me -> owned Tasks only",
    [
        "Permissions consistent across endpoints",
        "Seed two users for demo",
    ],
    [
        "Full flow demo",
        "Navbar shows user + logout",
    ],
    ["Anonymous cannot CRUD", "Ownership holds"],
    ["Leaving AllowAny on write endpoints"],
)

# --- Block E ---
write(
    "S33_shop_erd.md",
    "S33 — Shop ERD: Product, Category, Order",
    "Design Mini Shop ERD before coding.",
    "Category 1:N Product\n"
    "Order 1:N OrderItem N:1 Product\n"
    "Customer/User on Order",
    [
        "Finalize field list (price, stock, status)",
        "No models until ERD approved by instructor",
    ],
    ["List pages you will build: products, product form, orders, create order"],
    ["ERD signed off", "Page/API list written"],
    ["Coding models before relationships are clear"],
)

write(
    "S34_products_table.md",
    "S34 — Products table + image URL + filter by category",
    "List products with category filter.",
    "image_url as URLField/CharField for class simplicity (no media upload yet).",
    [
        "Product + Category models + APIs",
        "Filter ?category=",
    ],
    [
        "Products table page",
        "Thumbnail from image_url",
        "Category filter",
    ],
    ["Table loads", "Filter works"],
    ["Broken image URLs — use placeholder"],
)

write(
    "S35_product_form.md",
    "S35 — Product create/edit form (FK id)",
    "Create and edit products including category id.",
    "Write serializer accepts category as PK.\n"
    "Read serializer may expose category_name.",
    [
        "Create/update product endpoints",
        "Validation: price >= 0, stock >= 0",
    ],
    [
        "ProductForm page",
        "Edit mode loads detail then PATCH",
    ],
    ["Create + edit work", "Validation errors shown"],
    ["Sending nested category object by mistake"],
)

write(
    "S36_orders_list.md",
    "S36 — Orders list with join-style serializer fields",
    "List orders with readable related fields.",
    "SerializerMethodField or source= for product_name, username, total",
    [
        "Order + OrderItem models",
        "List serializer with denormalized display fields",
    ],
    ["Orders table page"],
    ["Orders show product names / totals", "Empty state ok"],
    ["Exposing huge nested trees when a flat list is enough"],
)

write(
    "S37_order_create.md",
    "S37 — Order create flow + line items",
    "Create an order with one or more line items in one API call.",
    "Writable nested serializer or explicit service in create()\n"
    "Use transaction.atomic()",
    [
        "POST /api/orders/ with items: [{product_id, qty}]",
        "atomic create Order + OrderItems",
    ],
    [
        "Create Order page: pick products + qty",
        "Redirect to orders list on success",
    ],
    ["Order + items appear together", "Failure rolls back (no half order)"],
    ["Creating items without transaction"],
)

write(
    "S38_stock_rules.md",
    "S38 — Stock update API + business rules",
    "Decrease stock when ordering; reject overselling.",
    "Business rules live in serializer/view/service — not only in the UI.",
    [
        "On order create: check stock, decrement",
        "400 if qty > stock",
    ],
    ["Show error when stock insufficient", "Refresh product stock on products page"],
    ["Stock decreases correctly", "Oversell blocked"],
    ["Race conditions — mention select_for_update for advanced"],
)

write(
    "S39_permissions.md",
    "S39 — Admin vs API roles (staff flag)",
    "Restrict product write to staff; orders for authenticated users.",
    "request.user.is_staff\n"
    "IsAdminUser vs custom permission class",
    [
        "Product create/update/delete: staff only",
        "Orders: authenticated owner",
    ],
    [
        "Hide admin buttons for non-staff",
        "Still enforce on API (UI hide is not security)",
    ],
    ["Non-staff gets 403 on product write", "Staff can manage catalog"],
    ["Trusting only frontend role checks"],
)

write(
    "S40_shop_review.md",
    "S40 — Mini Shop review + end-to-end demo",
    "Demo catalog + order + stock + roles.",
    "Full path: staff adds product -> user orders -> stock updates",
    ["Seed staff + normal user", "Fix permission gaps"],
    ["Scripted demo for class"],
    ["All four shop pages work", "Rules hold under wrong-role attempts"],
    ["Demo data missing — seed first"],
)

# --- Block F ---
write(
    "S41_capstone_plan.md",
    "S41 — Capstone: pick theme + ERD + page/API list",
    "Choose Blog, Helpdesk, or Classroom and plan before coding.",
    "Capstone is page-by-page — not a timed hackathon.",
    [
        "Approve ERD with instructor",
        "List endpoints per page",
    ],
    ["List React routes + which API each calls"],
    ["Theme chosen", "ERD + API list complete"],
    ["Scope too big — cut to 3–4 pages max"],
)

write(
    "S42_capstone_models.md",
    "S42 — Capstone: models + seed data",
    "Implement models/migrations and seed sample rows.",
    "Seed via management command or Admin fixtures.",
    [
        "Models from ERD",
        "migrate",
        "Seed 5–10 realistic rows",
    ],
    ["Confirm data via Admin or early list API"],
    ["Migrations clean", "Seed data visible"],
    ["Editing migrations by hand unnecessarily"],
)

write(
    "S43_capstone_auth_layout.md",
    "S43 — Capstone: auth + main layout",
    "Reuse JWT auth and build app shell (nav/sidebar).",
    "Copy patterns from Block D; do not reinvent auth.",
    ["Reuse token auth settings", "Protect APIs"],
    [
        "Login/register if needed",
        "Layout with nav to all planned pages",
    ],
    ["Logged-in shell works", "Logout works"],
    ["Forking a new auth scheme mid-capstone"],
)

write(
    "S44_capstone_table.md",
    "S44 — Capstone: main table + pagination",
    "Ship the primary list page with pagination.",
    "Same skills as S20 — applied to your domain.",
    ["Paginated list endpoint"],
    ["Table page with next/prev or page numbers"],
    ["Table loads with seed data", "Page 2 works"],
    ["Client-only paging with huge payloads"],
)

write(
    "S45_capstone_detail.md",
    "S45 — Capstone: detail + related data",
    "Detail page with nested or related resources.",
    "Reuse nested serializer patterns from S19.",
    ["Detail endpoint + related"],
    ["Detail route wired from table row click"],
    ["Detail shows related objects"],
    ["Dead links from table to detail"],
)

write(
    "S46_capstone_forms.md",
    "S46 — Capstone: forms + validation",
    "Create/edit forms with server-side validation shown in UI.",
    "Always validate on server; UI validation is helper only.",
    ["Write serializers with clear errors"],
    ["Create + edit forms", "Display field errors"],
    ["Happy path + validation path both work"],
    ["Only validating in React"],
)

write(
    "S47_deploy_checklist.md",
    "S47 — Deploy basics / production-like checklist",
    "Prepare a local production-like checklist; mention PostgreSQL.",
    "DEBUG=False, SECRET_KEY from env, ALLOWED_HOSTS,\n"
    "CORS origins, collectstatic if needed,\n"
    "SQLite ok for class; PostgreSQL for real deploy.",
    [
        "Move secrets to environment variables",
        "Document run instructions in project README",
    ],
    ["Build frontend: npm run build (discuss serving options)"],
    ["Checklist filled", "App still runs with safer settings locally"],
    ["Committing .env with secrets"],
)

write(
    "S48_demo_day.md",
    "S48 — Demo day + 48-session checklist",
    "Present capstone and reflect on skills gained.",
    "Demo script: problem -> ERD -> API -> pages -> auth/rules.",
    ["Ensure seed + two roles ready for live demo"],
    ["5–7 minute demo per student/team"],
    [
        "Demo completed",
        "Self-check: HTTP, ERD, CRUD API, React pages, JWT, ownership, validation",
    ],
    ["Live-coding unfinished features during demo — freeze scope night before"],
)

print(f"Wrote {len(list(BASE.glob('S*.md')))} session files to {BASE}")
