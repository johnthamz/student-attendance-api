# Student Attendance Management API

A backend REST API built with Django and Django REST Framework to manage students, classrooms, enrollments, and attendance records for educational institutions.

This project was developed as a capstone backend project and demonstrates clean API design, role-based permissions, and real-world backend workflows.

---

## Project Overview

The Student Attendance Management API allows institutions to:

- Manage users (Admins and Teachers)
- Register students
- Create classrooms
- Enroll students into classrooms
- Record attendance (single and bulk)
- Generate attendance reports

This is a backend-only project, intended to be consumed by a frontend web or mobile application.



## Tech Stack

- Python 3
- Django
- Django REST Framework
- SQLite (development database)
- Git & GitHub

---

##  Project Structure

```text
student_attendance_api/
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── students/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── classes/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── attendance/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── reports/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── README.md
└── venv/
```

---

##  Authentication & Permissions

The system implements role-based access control.

### User Roles

- Admin
  - Full access to the system
  - Can manage all resources

- Teacher
  - Can manage attendance
  - Can view reports
  - Limited administrative permissions

### Permissions Used

- `IsAuthenticated` → Restricts access to logged-in users
- `IsTeacher` → Custom permission allowing only teachers to access certain endpoints

---

##  Core Features

### 1️ User & Authentication
- Custom user model
- Teacher profiles
- Secure access using Django authentication

---

### 2️ Student Management
- Create students
- List all students
- Retrieve student details

---

### 3️ Classroom Management
- Create classrooms
- Assign teachers to classrooms
- List classrooms

---

### 4️ Enrollment Management
- Enroll students into classrooms
- Prevent duplicate enrollments
- Maintain student–class relationships

---

### 5️ Attendance Management

#### Attendance Sessions
- Create attendance sessions for classrooms

#### Attendance Records
- Mark individual student attendance

#### Bulk Attendance Endpoint
- Submit attendance records for multiple students in a single request
- Optimized for performance

---

### 6️ Reports API
- Generate attendance reports
- Retrieve attendance data across sessions
- Ready for analytics and dashboards

---

##  API Endpoints (Summary)

 Feature             Endpoint 

 Students            `/api/students/` 
 Student Detail      `/api/students/<id>/` 
 Classrooms          `/api/classes/` 
 Enrollments          `/api/enrollments/` 
 Attendance Sessions  `/api/attendance/sessions/` 
 Bulk Attendance      `/api/attendance/bulk/` 
 Attendance Reports   `/api/reports/attendance/` 



##  Development Setup

### Clone Repository
```bash
git clone https://github.com/johnthamz/student_attendance_api.git
cd student_attendance_api
```

### Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install django djangorestframework
```

### Apply Migrations
```bash
python manage.py migrate
```

### Run Development Server
```bash
python manage.py runserver
```

---

##  Future Improvements

- JWT authentication
- API pagination and filtering
- Frontend integration
- Cloud deployment (Render / Railway / AWS)

---

##  Author

**John Mithamo**  
Backend Development Student  

GitHub: https://github.com/johnthamz
