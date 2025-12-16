# Student Attendance Management API

## 📌 Project Overview
This is a backend REST API for managing student attendance in a school environment.  
The system allows administrators and teachers to manage students, classrooms, enrollments, and attendance records in a structured and scalable way.

This project was built as a **Capstone Project for a Backend Development course** and is designed to demonstrate real-world backend concepts such as database modeling, authentication, and RESTful APIs.

---

## 🚀 Features Implemented 

- Custom User model (Admin & Teacher roles)
- Teacher profile management
- Student management (Admission number as primary key)
- Classroom management with assigned class teachers
- Student enrollment with transfer history
- Attendance sessions (Morning / Afternoon)
- Individual attendance records (Present / Absent)
- Django Admin panel integration
- Clean, normalized database design based on ERD

---

## 🧱 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (Development)
- Git & GitHub

---

## 🗂 Project Structure

```text
student_attendance_api/
├── accounts/        # Custom user & authentication logic
├── students/        # Student & enrollment models
├── classes/         # Classroom management
├── attendance/      # Attendance sessions & records
├── reports/         # Reporting (future)
├── config/          # Project settings & URLs
├── manage.py
└── README.md
