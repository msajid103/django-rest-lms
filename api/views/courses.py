from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from courses.models import Course
from api.serializers.courses import CourseSerializer

@api_view(["GET","POST"])
def courseView(request):
    if request.method == "GET":
        course = Course.objects.all()
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer= CourseSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def courseDetailView(request, id):
    course = get_object_or_404(Course, id=id)
    
    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)



    elif request.method == "PUT":
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

