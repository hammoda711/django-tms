from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from unittest.mock import patch
from .models import Course

User = get_user_model()

class CourseViewsTestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        """
        Set up initial test data (runs once for all test cases).
        """
        cls.admin_user = User.objects.create_superuser(email='admin@example.com', password='admin123', role="admin")
        cls.regular_user = User.objects.create_user(email='user@example.com', password='user123', role='trainer')

        # Generate JWT tokens for authentication
        cls.admin_token = str(AccessToken.for_user(cls.admin_user))
        cls.user_token = str(AccessToken.for_user(cls.regular_user))

        # Sample Course
        cls.course = Course.objects.create(title="Test Course", description="Test Description", date="2024-12-01T12:00:00Z")


    def authenticate(self, is_admin=False):
        """
        Authenticate the request by setting a valid JWT token.
        """
        token = self.admin_token if is_admin else self.user_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        

    @patch('courses.services.CourseService.get_all_courses')
    def test_list_courses(self, mock_get_all_courses):
        """
        Test retrieving all courses (public access).
        """
        mock_get_all_courses.return_value = [self.course]  # Mock service return value

        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0]) 


    @patch('courses.services.CourseService.get_course_by_id')
    def test_get_course_detail(self, mock_get_course_by_id):
        """
        Test retrieving a specific course (public access).
        """
        mock_get_course_by_id.return_value = self.course

        response = self.client.get(f'/api/courses/{self.course.id}/detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Course")


    @patch('courses.services.CourseService.create_course')
    def test_create_course_as_admin(self, mock_create_course):
        """
        Test course creation (only admins allowed).
        """
        self.authenticate(is_admin=True)  # Authenticate as admin

        # Create a mock return value with the expected new course
        mock_created_course = Course(
            title="New Course",
            description="New Description",
            date="2024-12-01T12:00:00Z"
        )
        mock_create_course.return_value = mock_created_course  # Use the new mock course

        data = {
            "title": "New Course",
            "description": "New Description",
            "date": "2024-12-01T12:00:00Z"
        }
        response = self.client.post('/api/courses/create/', data, format='json')  # Ensure correct URL and JSON format
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Course")  # Now it should match


    def test_create_course_as_non_admin(self):
        """
        Test that non-admin users cannot create a course.
        """
        self.authenticate(is_admin=False)  # Authenticate as a regular user

        data = {
            "title": "Unauthorized Course",
            "description": "Should not be created",
            "date": "2024-12-01T12:00:00Z"
        }
        response = self.client.post('/api/courses/create/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) 


    @patch('courses.services.CourseService.update_course')
    def test_update_course_as_admin(self, mock_update_course):
        """
        Test updating a course (only admins allowed).
        """
        self.authenticate(is_admin=True)

        updated_course = Course.objects.create(title="Updated Course", description="Updated Description", date="2024-12-02T12:00:00Z")
        mock_update_course.return_value = updated_course

        data = {
            "title": "Updated Course",
            "description": "Updated Description",
            "date": "2024-12-02T12:00:00Z"
        }
        response = self.client.patch(f'/api/courses/{self.course.id}/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Course")


    def test_update_course_as_non_admin(self):
        """
        Test that non-admin users cannot update a course.
        """
        self.authenticate(is_admin=False)

        data = {
            "title": "Attempted Update",
            "description": "Should not be allowed",
            "date": "2024-12-02T12:00:00Z"
        }
        response = self.client.patch(f'/api/courses/{self.course.id}/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    @patch('courses.services.CourseService.delete_course')
    def test_delete_course_as_admin(self, mock_delete_course):
        """
        Test deleting a course (only admins allowed).
        """
        self.authenticate(is_admin=True)
        mock_delete_course.return_value = None  # Simulating successful deletion
        response = self.client.delete(f'/api/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_delete_course_as_non_admin(self):
        """Test that non-admin users cannot delete a course."""
        self.authenticate(is_admin=False)
        response = self.client.delete(f'/api/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
