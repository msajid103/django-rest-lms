from django.urls import path
from .views import courses, teachers


urlpatterns = [
    # course url path and these are function based
    path('courses/', courses.courseView),
    path('courses/<int:id>', courses.courseDetailView),

    # teacher url path and these are class based views
    path('teachers/', teachers.Teachers.as_view()),
    path('teachers/<int:id>', teachers.TeacherDetail.as_view())
]