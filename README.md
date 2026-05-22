🏥 MediCore HMS v3 — Hospital Management System
A modern Hospital Management System built with Django REST Framework and a lightweight frontend SPA.
The project supports patient record management, billing, dashboard statistics, and works in both online and offline demo mode.
🚀 Features
✅ Patient Records Management
✅ Billing & Payment Tracking
✅ Dashboard Statistics APIs
✅ Django REST Framework Backend
✅ Single Page Frontend (SPA)
✅ Offline Demo Mode Support
✅ Admin Panel Access
✅ Demo Seed Data Included
📁 Project Structure
Bash
hospital_project/
├── backend/
│   ├── records/              # Patient records app
│   ├── billing/              # Billing management app
│   ├── backend/              # Django settings & URLs
│   ├── manage.py
│   ├── seed.py               # Demo data loader
│   └── requirements.txt
│
└── frontend/
    └── index.html            # Frontend SPA
⚡ Quick Start
1️⃣ Navigate to Backend
Bash
cd hospital_project/backend
2️⃣ Install Dependencies
Bash
pip install -r requirements.txt
3️⃣ Create Migrations
Bash
python manage.py makemigrations records
python manage.py makemigrations billing
4️⃣ Apply Migrations
Bash
python manage.py migrate
5️⃣ Load Demo Data
Bash
python seed.py
This loads:
7 Demo Patients
4 Demo Bills
6️⃣ Run Development Server
Bash
python manage.py runserver
🌐 Application URLs
Service
URL
Frontend App
http://127.0.0.1:8000/
Records API
http://127.0.0.1:8000/api/records/
Billing API
http://127.0.0.1:8000/api/billing/
Admin Panel
http://127.0.0.1:8000/admin/
👤 Create Admin User (Optional)
Bash
python manage.py createsuperuser
Then login at:
Bash
http://127.0.0.1:8000/admin/
🔌 API Endpoints
📋 Patient Records
Method
Endpoint
Description
GET / POST
/api/records/
List or create patients
GET
/api/records/stats/
Dashboard statistics
GET / PUT / DELETE
/api/records/<id>/
Patient details
💳 Billing
Method
Endpoint
Description
GET / POST
/api/billing/
List or create bills
GET
/api/billing/stats/
Revenue statistics
POST
/api/billing/<id>/mark-paid/
Mark bill as paid
💡 Important Notes
The frontend supports offline mode
Demo data is automatically used if the backend is unavailable
The green status indicator in the sidebar shows API connectivity
Billing uses patient record ID (record) instead of patient name when connected to backend APIs
🛠️ Tech Stack
Backend
Python
Django
Django REST Framework
SQLite
Frontend
HTML
CSS
JavaScript
📦 Requirements
Install all dependencies using:
Bash
pip install -r requirements.txt
📸 Demo Workflow
Start Django server
Open frontend in browser
Add/view patients
Create bills
Mark bills as paid
Monitor statistics dashboard
✅ Future Improvements
Authentication & Authorization
JWT Login System
Doctor Management
Appointment Scheduling
PDF Bill Generation
Email Notifications
Advanced Analytics Dashboard
📄 License
This project is developed for educational and demonstration purposes.
👨‍💻 Author
MediCore HMS v3
Hospital Management System using Django REST Framework and SPA frontend