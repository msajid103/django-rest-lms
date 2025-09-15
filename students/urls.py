from django.urls import path
from . import views

urlpatterns=[
    path('',views.get_students),
    path('<int:id>/',views.get_student),
    path('create-student/',views.create_student),
    path('update-student/<int:id>/',views.update_student),
    path('delete-student/<int:id>/',views.delete_student),
]