from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.repositories import CourseRepository
from trainers.permissions import IsOwnerOrAdmin
from .serializers import CourseSerializer, CourseTrainerSerializer
from .services import CourseService
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied

class CourseListView(APIView):
    """
    View to list courses.
    """
    permission_classes = [IsAdminUser]

    def get(self, request):
        service = CourseService()
        courses = service.get_all_courses()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CourseDetailView(APIView):
    """
    View to retrieve, a specific course.
    """
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request, course_id):
        service = CourseService()
        try:
            course = service.get_course_by_id(course_id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class CourseCreateView(APIView):
    """
    View to create a new course. Only accessible by admins.
    """
    permission_classes = [IsAdminUser]

    def post(self, request):
        service = CourseService()
        try:
            course = service.create_course(
                request.data['title'], 
                request.data['description'], 
                request.data['date'],
            )
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CourseUpdateDeleteView(APIView):
    """
    View to retrieve or delete a new course. Only accessible by admins.
    """
    permission_classes = [IsAdminUser]
    
    def patch(self, request, course_id):
        service = CourseService()
        try:
            course = service.update_course(
                course_id, 
                request.data['title'], 
                request.data['description'], 
                request.data['date'], 
            )
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_id):
        service = CourseService()
        try:
            service.delete_course(course_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

class LinkTrainerToCourseView(APIView):
    """
    View to link multiple trainers to a course.
    """
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        trainer_ids = request.data.get('trainer_ids', [])

        # Fetch the course
        course = CourseRepository.get_course_by_id(course_id)
        if not course:
            raise NotFound("Course not found.")

        # Link multiple trainers
        updated_course = CourseService.link_trainers_to_course(course, trainer_ids)

        return Response(CourseTrainerSerializer(updated_course).data)