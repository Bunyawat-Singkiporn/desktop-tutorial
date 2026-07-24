# Starter backend — Django + DRF + CORS + SimpleJWT

## Setup

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- API: http://127.0.0.1:8000/api/tasks/
- Admin: http://127.0.0.1:8000/admin/
- JWT: POST http://127.0.0.1:8000/api/auth/token/

Early sessions keep `AllowAny`. From Block D, switch default permission to `IsAuthenticated`.
