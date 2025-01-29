from django.urls import path
from .views import CourseListView, CourseCreateView, CourseDetailView, CourseUpdateDeleteView, LinkTrainerToCourseView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:course_id>/detail/', CourseDetailView.as_view(), name='course-detail'),
    path('<int:course_id>/', CourseUpdateDeleteView.as_view(), name='course-update-delete'),
    path('link-trainers-to-course/', LinkTrainerToCourseView.as_view(), name='link-trainers-to-course'),

]
