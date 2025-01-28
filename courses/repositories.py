from .models import Course
from django.db import transaction

class CourseRepository:
    """
    This repository handles the data access logic for Course model.
    """

    def get_all_courses(self):
        return Course.objects.all()

    def get_course_by_id(self, course_id):
        return Course.objects.get(id=course_id)

    def create_course(self, title, description, date):
        # Create a new course
        course = Course.objects.create(
            title=title, 
            description=description,
            date=date,
        )
        return course

    def update_course(self, course, title, description, date):
        course.title = title
        course.description = description
        course.date = date
        course.save()
        return course

    def delete_course(self, course):
        course.delete()
