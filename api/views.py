from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt, name ='dispatch')

class StudentAPI(View):
	def get(self, request, *args, **kwargs):
		
		json_data = request.body
		stream = io.BytesIO(json_data)
		pydata = JSONParser().parse(stream)
		id = pydata.get('id',None)
		if id is not None:
			stu = Student.objects.get(id = id)
			serial = StudentSerializer(stu)
			return JsonResponse(serial.data,safe = False)

		stu = Student.objects.all()
		serial = StudentSerializer(stu , many = True)
		return JsonResponse(serial.data, safe = False)

	def post(self, request, *args, **kwargs):
		
		json_data = request.body
		stream = io.BytesIO(json_data)
		pydata = JSONParser().parse(stream)
		serial = StudentSerializer(data = pydata)
		if serial.is_valid():
			serial.save()
			msg ={'data' : 'saved'}
			return JsonResponse(msg, safe = False)
		return JsonResponse(serial.errors, safe = False)

	def put(self, request, *args, **kwargs):
		
		json_data =  request.body
		stream = io.BytesIO(json_data)
		pydata = JSONParser().parse(stream)
		id = pydata.get('id')
		Stu = Student.objects.get(id = id)
		serial = StudentSerializer(Stu, data = pydata, partial = True)

		if serial.is_valid():
			serial.save()
			msg = {'data' : 'updated!!'}
			return JsonResponse(msg,safe = False)
		return JsonResponse(serial.errors, safe = False)

	def delete(self, request, *args, **kwargs):
		
		json_data =  request.body
		stream = io.BytesIO(json_data)
		pydata = JSONParser().parse(stream)
		id = pydata.get('id')
		Stu = Student.objects.get(id = id)
		Stu.delete()

		msg = {'data' : 'Deleted!!'}
		return JsonResponse(msg,safe = False)


	


	

	
		


