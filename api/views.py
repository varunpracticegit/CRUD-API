from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Condition for Reading/getting data
@csrf_exempt
def student_api(request):
 if request.method == 'GET':
   json_data = request.body
   stream = io.BytesIO(json_data)
   pythondata = JSONParser().parse(stream)
   id = pythondata.get('id', None)
   if id is not None:
     stu  = Student.objects.get(id=id)
     serializer = StudentSerializer(stu)
     json_data = JSONRenderer().render(serializer.data)
     return HttpResponse(json_data, content_type='application/json')   
   
   stu = Student.objects.all()
   serializer = StudentSerializer(stu, many=True)
   json_data = JSONRenderer().render(serializer.data)
   return HttpResponse(json_data, content_type='application/json')  
 

 # Condition for creating data
 if request.method == 'POST':
   json_data = request.body
   stream = io.BytesIO(json_data)
   pythondata = JSONParser().parse(stream)
   serializer = StudentSerializer(data=pythondata)
   if serializer.is_valid():
     serializer.save()
     res = {'msg':'Data Created'}
     json_data = JSONRenderer().render(res)
     return HttpResponse(json_data, content_type='application/json')
   json_data = JSONRenderer().render(serializer.errors)
   return HttpResponse(json_data, content_type='application/json')


 # Condition for updating data

 if request.method == 'PUT':
   json_data = request.body
   stream = io.BytesIO(json_data)
   pythondata = JSONParser().parse(stream)
   id = pythondata.get('id')
   stu = Student.objects.get(id=id)
   serializer = StudentSerializer(stu, data=pythondata, partial=True)
   if serializer.is_valid():
     serializer.save()
     res = {'msg':'Data Upated'}
     json_data = JSONRenderer().render(res)
     return HttpResponse(json_data, content_type='application/json')
   json_data = JSONRenderer().render(serializer.errors)
   return HttpResponse(json_data, content_type='application/json')
 

 # Condition for deleting data

 if request.method == 'DELETE':
   json_data = request.body
   stream = io.BytesIO(json_data)
   pythondata = JSONParser().parse(stream)
   id = pythondata.get('id')
   stu = Student.objects.get(id=id)
   stu.delete()
   res = {'msg':'Data Deleted'}
   json_data = JSONRenderer().render(res)
   return HttpResponse(json_data, content_type='application/json')
