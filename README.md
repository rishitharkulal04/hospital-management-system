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
| GET / POST | `/api/records/` | List or create patients |
| GET | `/api/records/stats/` | Dashboard statistics |
| GET / PUT / DELETE | `/api/records/<id>/` | Patient details |

---

## 💳 Billing

| Method | Endpoint | Description |
|---|---|---|
| GET / POST | `/api/billing/` | List or create bills |
| GET | `/api/billing/stats/` | Revenue statistics |
| POST | `/api/billing/<id>/mark-paid/` | Mark bill as paid |

---

# 💡 Notes

- The frontend works in **offline mode** if the backend is not running
- Demo data is automatically used in offline mode
- The green indicator in the sidebar shows API connection status
- Billing uses `record` (patient ID) instead of patient name when connected to backend APIs

---

# 🛠️ Tech Stack

## Backend
- Python
- Django
- Django REST Framework
- SQLite

## Frontend
- HTML
- CSS
- JavaScript

---

# 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

# 📸 Demo Workflow

1. Start Django server
2. Open frontend in browser
3. Add or view patients
4. Create bills
5. Mark bills as paid
6. View dashboard statistics

---

# 🔮 Future Improvements

- Authentication System
- JWT Login
- Doctor Management
- Appointment Scheduling
- PDF Bill Generation
- Email Notifications
- Analytics Dashboard

---

# 📄 License

This project is developed for educational and demo purposes.

---

# 👨‍💻 Author

**MediCore HMS v3**  
Hospital Management System using Django REST Framework and SPA frontend.