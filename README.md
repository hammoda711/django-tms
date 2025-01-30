# Django Course Training Management System

---------

## Documentation Files:

1. [API Endpoints](documentation/API_ENDPOINTS.md):

2. [Testing Guide](documentation/TESTS.md) 

3. [Postman Collection](documentation/Postman_Collection.json) 

------------

## **1. Project Overview**

### Description

This Django-based web application is designed for managing courses and trainers within a training company. The system allows admins to perform CRUD operations on courses and trainers, assign trainers to courses, manage payments, and generate rewards efficiently. 

### Design Patterns

The project follows the **Repository Pattern** and **Service Pattern**, ensuring a clean and modular architecture:

- **Repository Pattern**: Used to abstract database operations, keeping queries separate from business logic. This improves maintainability, makes testing easier, and reduces duplication.
- **Service Pattern**: Encapsulates business logic in dedicated service classes, making views/controllers lean and ensuring separation of concerns.

### **Project Structure**

The application follows a **multiple Django app single project** structure, where each domain (trainers, courses, payments) is a separate Django app. Each app is self-contained.

### **Authentication**

The project uses **Simple JWT** for authentication, ensuring secure token-based access. Key authentication features include:

- **Access and Refresh Tokens**: Used to authenticate users securely.
- **JWT Token Handling**: Tokens are generated at login and passed in the `Authorization` header for authenticated requests.

### **Technology Stack**:

- **Backend**: Django, Django REST Framework (DRF)

- **Database**: SQLite3

- **Authentication**: Simple JWT (JSON Web Token)

---------------

## **2. Installation and Setup**

### **Installation Steps**:

- Clone the repo.

- `git clone https://github.com/hammoda711/django-tms.git`

- Set up a virtual environment.

- `py -m venv venv`

- Install dependencies using

- `pip install -r requirements.txt`.

- Configure environment variables: 
  
  `.env.example`
  
  ```.env
  SECRET_KEY=""
  DEBUG=
  ALLOWED_HOSTS=localhost,127.0.0.1
  ```

- Run migrations `py manage.py migrarte`

- start the server `py manage.py runserver`

------------

## 3. Functionality Overview

The system supports CRUD (Create, Read, Update, Delete) operations for courses, trainers, and payments. These operations are role-dependent, ensuring that only authorized users can perform certain actions.

### Role-Based Access

- **Admin**:
  - Full access to **CRUD operations** on **courses** and **trainers**, except for updating personal details of trainer profiles.
  - Can **assign trainers to courses** and manage payment records.
- **Trainer**:
  - Can only **view** courses they are assigned to.
  - Can **update personal information** in their own profile.
  - Can **list payments** they have received but cannot modify or delete them.

----------

## **4. API Documentation**

- For detailed API documentation, including all available endpoints, request methods, parameters, and responses, please refer to the **[API Documentation](documentation/API_ENDPOINTS.md)** file located in the `documentation` directory in the project.

- You can also use `postman` by [Viewing API Collection Docs in Postman](https://documenter.getpostman.com/view/38668715/2sAYQiB7ae) or you can refer to the [<u>Postman Collection JSON File</u>](documentation/Postman_Collection.json) in the `documentaion` directory in the project.

----------

## **5. Testing**

### **Testing Framework**

The test cases in this project are built using **Django REST Framework's Test Framework**. 

- **`APITestCase`**: All test cases are derived from `APITestCase`, which extends Django's standard `TestCase` and provides methods to send HTTP requests, check the response status, and verify data returned from the API.
- **`self.client`**: The test suite uses the built-in `self.client` to simulate HTTP requests and capture responses. 

### Running Tests

To run the test suite, use the following commands:

```bash
python manage.py test courses #replace with the app you want to test
```

### Test Guide

You can find the detailed guide for all test cases in our project in [Test Guide.md](documentation/TESTS.md).

-------
