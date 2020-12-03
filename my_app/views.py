from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
#creating RestApi view of Teacher model

class teacherList(APIView):
    def get(self,request):
        teacher1 = Teacher.objects.all()
        serializer = teacherSerializer(teacher1,many=True)

        return Response(serializer.data)
    def post(self,request):
        pass

#creating RestApi view of Student model

class studentList(APIView):
    def get(self,request):
        student1 = Student.objects.all()
        serializer = studentSerializer(student1,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass