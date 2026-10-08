````markdown
# Doctor Appointment Management System

A Django REST Framework based backend application for managing doctors and patient appointments through REST APIs.

## Features

- Doctor management
  - Create doctor
  - View all doctors
  - View individual doctor
  - Update doctor details
  - Delete doctor

- Appointment management
  - Create appointments
  - View appointments
  - View individual appointments
  - Update appointments
  - Delete appointments

- User registration
- Admin registration
- Authentication for protected API endpoints
- RESTful API design using Django REST Framework

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Git & GitHub

## Project Structure

```text
doctor_appoinments_crud_django/
│
├── booking_v2/
├── bookings/
├── care_connect/
├── staff/
├── staff_v2/
├── APIDOC.http
├── db.sqlite3
├── manage.py
└── .gitignore
````

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aravindbalaji4851-cmd/doctor_appoinments_crud_django.git
```

### 2. Navigate to the project directory

```bash
cd doctor_appoinments_crud_django
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install django djangorestframework
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Doctor APIs

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| GET    | `/doctors/`      | List doctors           |
| POST   | `/doctors/`      | Create a doctor        |
| GET    | `/doctors/<id>/` | View a specific doctor |
| PUT    | `/doctors/<id>/` | Update a doctor        |
| DELETE | `/doctors/<id>/` | Delete a doctor        |

### Appointment APIs

| Method | Endpoint         | Description           |
| ------ | ---------------- | --------------------- |
| GET    | `/appointments/` | List appointments     |
| POST   | `/appointments/` | Create an appointment |

### Authenticated APIs

The project also includes protected `v2` endpoints for doctor and appointment management.

#### User Registration

```text
POST /v2/booking/signup/
```

Example request:

```json
{
    "username": "django",
    "email": "django@gmail.com",
    "password": "django"
}
```

#### Appointment Management

```text
GET    /v2/booking/appointments/
POST   /v2/booking/appointments/
GET    /v2/booking/appointments/<id>/
PUT    /v2/booking/appointments/<id>/
DELETE /v2/booking/appointments/<id>/
```

Authentication is required for these protected endpoints.

## Example Appointment Request

```json
{
    "patient_name": "Ajay",
    "phone": "123456789",
    "doctor": 1,
    "appointment_date": "2026-10-11",
    "problem": "cold"
}
```

## API Testing

The repository contains an `APIDOC.http` file with sample API requests that can be used to test the endpoints using an HTTP client such as the REST Client extension in Visual Studio Code.

## Learning Objectives

This project was developed to practice:

* Django REST Framework
* CRUD operations
* Django models
* Serializers
* API views
* Database operations
* Authentication
* REST API development
* Working with related models

## Author

**Aravind Balaji K J**

GitHub: https://github.com/aravindbalaji4851-cmd

```
```
