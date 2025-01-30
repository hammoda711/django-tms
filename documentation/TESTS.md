# Testing Guide

---

## **Testing Framework**

The test cases in this project are built using **Django REST Framework's Test Framework**. The framework provides a convenient and robust environment for testing RESTful APIs, ensuring that the endpoints work as expected under various conditions.

- **`APITestCase`**: All test cases are derived from `APITestCase`, which extends Django's standard `TestCase` and provides methods to send HTTP requests, check the response status, and verify data returned from the API.
- **`self.client`**: The test suite uses the built-in `self.client` to simulate HTTP requests and capture responses. This is used to test endpoints with different HTTP methods (GET, POST, PATCH, DELETE).
- **Authentication**: The tests utilize JWT tokens for authentication, ensuring that the relevant permissions and restrictions are applied according to the user's role.

-------

## Running Tests

To run the test suite, use the following command:

```bash
python manage.py test courses
python manage.py test trainers
python manage.py test payments
```

---

## **Courses API Test Cases**

### **Authentication Setup**

- **`setUpTestData(cls)`**: Sets up an admin and a regular user with JWT tokens.
- **`authenticate(self, is_admin=False)`**: Authenticates requests by setting a JWT token.

### **Test Cases**

**Admin Permissions Tests**  
These tests check that only admin users can create, update, and delete courses.

- **`test_create_course_as_admin`**: Verifies that an admin user can create a course.
- **`test_update_course_as_admin`**: Verifies that an admin user can update an existing course.
- **`test_delete_course_as_admin`**: Verifies that an admin user can delete a course.
- **`test_list_courses`**: Verifies that retrieving all courses.
- **`test_get_course_detail`**: Verifies that retrieving the details of a specific course.

**Non-Admin Permissions Tests**  
These tests ensure that non-admin users cannot perform restricted actions on courses.

- **`test_create_course_as_non_admin`**: Verifies that non-admin users cannot create a course.
- **`test_update_course_as_non_admin`**: Verifies that non-admin users cannot update a course.
- **`test_delete_course_as_non_admin`**: Verifies that non-admin users cannot delete a course.

---

## Trainers Test Cases

### **Authentication Setup**

- **`setUp(self)`**:  Sets up an admin user, a trainer user, and ensures the trainer user has a trainer profile. It also generates JWT tokens for both users.

- Ensures the trainer user is a trainer by creating a trainer profile if one does not already exist.

- Generates JWT tokens for both the admin and the trainer user.

#### **Admin Permissions Tests**

These tests ensure that admin users have full access to perform actions on trainer profiles, including creation, updating, and deletion.

- **`test_admin_can_create_trainer`**: Verifies that an admin user can create a new trainer profile.
- **`test_admin_can_retrieve_any_trainer`**: Verifies that an admin user can retrieve any trainer's profile.
- **`test_admin_can_update_trainer_restricted_fields`**: Verifies that an admin can update restricted fields (e.g., specialization) of a trainer profile.
- **`test_admin_can_delete_trainer`**: Verifies that an admin user can delete any trainer profile.
- **`test_admin_can_list_trainers`**: Verifies that an admin user can list all trainers.

#### **Trainer Permissions Tests**

These tests ensure that trainers have appropriate access to manage their own profiles and interact with the API accordingly.

- **`test_trainer_can_retrieve_own_profile`**: Verifies that a trainer can retrieve their own profile.
- **`test_trainer_can_update_own_profile`**: Verifies that a trainer can update their own profile information.
- **`test_trainer_can_list_own_trainings`**: Verifies that a trainer can view the list of training sessions they are managing (if applicable).

#### **Non-Admin Permissions Tests**

These tests check that non-admin users (including regular users) are restricted from performing actions that should only be available to admins or trainers.

- **`test_non_admin_cannot_create_trainer`**: Verifies that a non-admin user cannot create a trainer profile.
- **`test_non_admin_cannot_update_trainer_restricted_fields`**: Verifies that a non-admin user cannot update restricted fields of a trainer profile.
- **`test_non_admin_cannot_delete_trainer`**: Verifies that a non-admin user cannot delete a trainer profile.
- **`test_non_admin_cannot_list_trainers`**: Verifies that a non-admin user cannot list all trainers.
- **`test_user_cannot_retrieve_other_trainer_profile`**: Verifies that a regular user cannot retrieve the profile of another trainer.

#### **Profile Management Tests**

These tests focus on actions related to profile creation and updates, ensuring that users and admins can manage profiles properly.

- **`test_user_can_create_own_profile`**: Verifies that a regular user can create their own profile.
- **`test_trainer_can_update_own_profile`**: Verifies that a trainer can update their own profile.

#### **Miscellaneous Tests**

These tests include any other scenarios that do not fall under the above categories but are still important to verify.

- **`test_admin_can_retrieve_any_trainer`**: Verifies that an admin can retrieve any trainer’s profile.
- **`test_non_admin_cannot_retrieve_other_trainer_profile`**: Verifies that non-admin users cannot view other trainers’ profiles.

-------------

## **Payments API Test Cases**

#### **Authentication Setup**

- **`setUp(self)`**: Sets up an admin, regular user, and a trainer user with JWT tokens and creates a sample payment.
- **`authenticate(self, token)`**: Sets authentication using JWT tokens.

#### **Test Cases**

#### **Admin Permissions Tests**

These tests verify that admins can perform actions related to payments that regular users cannot.

- **`test_create_payment_as_admin`**: Verifies that an admin user can create a payment.
- **`test_list_payments_as_admin`**: Verifies that an admin user can list all payments.
- **`test_update_payment_status_as_admin`**: Verifies that an admin user can update the payment status.

#### **Trainer Permissions Tests**

These tests ensure that trainers can view their own payments but cannot perform administrative actions.

- **`test_list_payments_as_trainer`**: Verifies that a trainer can view their own payments.

#### **Non-Admin Permissions Tests**

These tests ensure that non-admin users are restricted from performing payment-related actions.

- **`test_create_payment_as_non_admin`**: Verifies that non-admin users cannot create payments.
- **`test_update_payment_status_as_non_admin`**: Verifies that non-admin users cannot update the payment status.

#### **Validation Tests**

These tests check that invalid payment updates are correctly rejected.

- **`test_update_payment_invalid_status`**: Verifies that updating the payment status with an invalid value is properly validated.

---
