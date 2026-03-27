# MediCore HMS v3 — Setup Guide

## ✅ QUICK START (5 commands)

```bash
cd hospital_project/backend
pip install -r requirements.txt
python manage.py makemigrations records
python manage.py makemigrations billing
python manage.py migrate
python seed.py          # loads 7 demo patients + 4 bills
python manage.py runserver
```

## 🌐 Open in Browser

- **Frontend App:** http://127.0.0.1:8000/   ← opens directly in browser (no 404!)
- **API Records:**   http://127.0.0.1:8000/api/records/
- **API Billing:**   http://127.0.0.1:8000/api/billing/
- **Admin Panel:**   http://127.0.0.1:8000/admin/

## 👤 Create Admin User (optional)
```bash
python manage.py createsuperuser
```

## 📁 Project Structure
```
hospital_project/
├── backend/          ← Django REST API
│   ├── records/      ← Patient records app
│   ├── billing/      ← Billing app
│   ├── backend/      ← Settings, URLs
│   ├── manage.py
│   ├── seed.py       ← Demo data loader
│   └── requirements.txt
└── frontend/
    └── index.html    ← Full SPA (served via Django at /)
```

## 🔌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | /api/records/ | List / create patients |
| GET | /api/records/stats/ | Dashboard statistics |
| GET/PUT/DELETE | /api/records/<id>/ | Patient detail |
| GET/POST | /api/billing/ | List / create bills |
| GET | /api/billing/stats/ | Revenue statistics |
| POST | /api/billing/<id>/mark-paid/ | Mark bill as paid |

## 💡 Notes
- The app works in **offline mode** even without the backend running (uses demo data)
- The green dot in the sidebar shows API connection status
- Bills use `record` (patient ID) — not patient name — when backend is online
