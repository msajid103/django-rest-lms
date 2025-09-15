import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed, JsonResponse
from students.models import Student
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


def get_students(request): 
   if request.method == "GET":
        students = Student.objects.all()
        data = [model_to_dict(student) for student in students ]
        return JsonResponse({"status":"success","count":len(data), "data":data}, safe=False)
   return HttpResponseNotAllowed(["GET"])
    
def get_student(request,id):
    if request.method == "GET":
        students = get_object_or_404(Student, id=id)
        data = model_to_dict(students)
        return JsonResponse({"status": "success", "data": data}, status=200)
    return HttpResponseNotAllowed(["GET"])
    
    
@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.create()
        for field, value in data.items():
            if hasattr(student, field):
                setattr(student,field,value)
        student.save() 
        return JsonResponse({"status":"success","message":"Student created","id":student.id},status=201)
    return HttpResponseNotAllowed(["POST"])
@csrf_exempt
def update_student(request,id):      
    if request.method in ["PUT","PATCH"]:
        student = get_object_or_404(Student, id=id)
        data = json.loads(request.body)
        for field, value in data.items():
            if hasattr(student,field):
                setattr(student, field, value)
        student.save()
        return JsonResponse({
            "status": "success",
            "message": "Student record updated",           
            "data": model_to_dict(student)
        }, status=200)
    return HttpResponseNotAllowed(["PUT","PATCH"])
@csrf_exempt
def delete_student(request,id):
    if request.method == "DELETE":
        student = get_object_or_404(Student, id=id)
        student.delete()
        return JsonResponse({"status":"success","message":"Student deleted"},status= 204)
    return HttpResponseNotAllowed(["DELETE"])


        