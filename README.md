# 🏥 MediCore HMS v3 — Hospital Management System

A modern Hospital Management System built with **Django REST Framework** and a lightweight frontend SPA.

The project supports:
- Patient Record Management
- Billing & Payment Tracking
- Dashboard Statistics
- Offline Demo Mode

---

# 🚀 Features

- ✅ Patient Records Management
- ✅ Billing System
- ✅ Revenue Statistics
- ✅ Django REST API
- ✅ Single Page Frontend (SPA)
- ✅ Offline Demo Support
- ✅ Admin Panel
- ✅ Demo Seed Data Included

---

# 📁 Project Structure

```bash
hospital_project/
├── backend/
│   ├── records/              # Patient records app
│   ├── billing/              # Billing app
│   ├── backend/              # Django settings & URLs
│   ├── manage.py
│   ├── seed.py               # Demo data loader
│   └── requirements.txt
│
└── frontend/
    └── index.html            # Frontend SPA
```

---

# ⚡ Quick Start

## 1️⃣ Navigate to Backend

```bash
cd hospital_project/backend
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Create Migrations

```bash
python manage.py makemigrations records
python manage.py makemigrations billing
```

## 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

## 5️⃣ Load Demo Data

```bash
python seed.py
```

This loads:
- 7 Demo Patients
- 4 Demo Bills

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

---

# 🌐 Application URLs

| Service | URL |
|---|---|
| Frontend App | http://127.0.0.1:8000/ |
| Records API | http://127.0.0.1:8000/api/records/ |
| Billing API | http://127.0.0.1:8000/api/billing/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

# 👤 Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

Then login at:

```bash
http://127.0.0.1:8000/admin/
```

---

# 🔌 API Endpoints

## 📋 Patient Records

| Method | Endpoint | Description |
|---|---|---|
| GET / POST | `/api/records/` | List