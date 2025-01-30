# API Documentation

The API provides functionalities for authentication, course management, trainer management, and payments, using **JWT authentication**.

### 🔗 Full API Documentation (Postman)

👉 [View API Collection Docs in Postman]([CTMS](https://documenter.getpostman.com/view/38668715/2sAYQiB7ae)) or you can use [Postman Collection JSON]() file

---

## Available Endpoints

### Authentication (`api/auth/`)

- `POST /api/auth/register/` → Register a new user
- `POST /api/auth/token/` → Obtain JWT access & refresh tokens
- `POST /api/auth/token/refresh/` → Refresh an access token

---

### Courses (`api/courses/`)

- `GET /api/courses/` → List all courses
- `POST /api/courses/create/` → Create a new course 
- `GET /api/courses/<int:course_id>/detail/` → Get details of a specific course
- `PATCH /api/courses/<int:course_id>/` → Update a course 
- `DELETE /api/courses/<int:course_id>/` → Delete a course 
- `POST /api/courses/link-trainers-to-course/` → Link trainers to a course

---

### Trainers (`api/trainers/`)

- `POST /api/trainers/create/` → Register a new trainer
- `GET /api/trainers/<int:pk>/` → Retrieve trainer profile
- `PATCH /api/trainers/<int:pk>/update-profile/` → Update trainer profile
- `PATCH /api/trainers/<int:pk>/update-admin/` → Admin updates trainer profile
- `DELETE /api/trainers/delete/<int:pk>/` → Delete a trainer
- `GET /api/trainers/` → List all trainers

---

### Payments (`api/payments/`)

- `POST /api/payments/create-payment/` → Create a payment
- `GET /api/payments/trainer/<int:trainer_id>/` → List all payments for a trainer
- `PATCH /api/payments/payment/<int:payment_id>/update/` → Update a payment
