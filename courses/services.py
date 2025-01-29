from trainers.models import Trainer
from trainers.repositories import TrainerRepository
from .repositories import CourseRepository
from django.core.exceptions import ObjectDoesNotExist

class CourseService:
    """
    Service layer handling the business logic for Course management.
    """

    def __init__(self):
        self.course_repo = CourseRepository()

    def get_all_courses(self):
        return self.course_repo.get_all_courses()

    def get_course_by_id(self, course_id):
        try:
            return self.course_repo.get_course_by_id(course_id)
        except ObjectDoesNotExist:
            raise ValueError(f"Course with ID {course_id} not found")

    def create_course(self, title, description, date):
        if not title or not description or not date:
            raise ValueError("All fields must be filled out")
        return self.course_repo.create_course(title, description, date)

    def update_course(self, course_id, title, description, date):
        try:
            course = self.course_repo.get_course_by_id(course_id)
        except ValueError:
            raise ValueError(f"Course with ID {course_id} not found")
        
        return self.course_repo.update_course(course, title, description, date)

    def delete_course(self, course_id):
        try:
            course = self.course_repo.get_course_by_id(course_id)
        except ValueError:
            raise ValueError(f"Course with ID {course_id} not found")
        
        self.course_repo.delete_course(course)
    
    #link trainers to courses
    @staticmethod
    def link_trainers_to_course(course, trainer_ids):
        trainers = Trainer.objects.filter(id__in=trainer_ids)
        course.trainers.add(*trainers)  # Bulk assign trainers
        return course