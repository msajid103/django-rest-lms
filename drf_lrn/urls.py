
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Stdudents app 
    path("students/",include('students.urls')),
    # api views
    path('api/v1/',include("api.urls")),
  
]
