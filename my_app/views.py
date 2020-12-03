from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required
from .decorators import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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

def home(request):
    return render(request,'home.html',)


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def teacher_home(request):
    return render(request,'teacher_home.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'One New student Added successfuly')
            return redirect('view_student')
    d = {'form':form}
    return render(request,'add_student.html',d)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def edit_student(request,pid):
    instance = get_object_or_404(Student, id=pid)
    form = StudentForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, 'One student Updated successfuly')
        return redirect('view_student')
    d = {'form':form}
    return render(request,'edit_student.html',d)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def view_student(request):
    student = Student.objects.all()
    d = {'student':student}
    return render(request,'view_student.html',d)

def Login_User(request):
    if request.method == "POST":
        u = request.POST['name']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            messages.success(request, 'Logged in successfuly')
            return redirect('teacher_home')
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        u = request.POST['name']
        p = request.POST['pwd']
        cp = request.POST['pwd2']
        sub = request.POST['subject']
        if p == cp:
            user = User.objects.create_user(username=u,password=p)
            Teacher.objects.create(user=user,subject=sub)
            messages.success(request, 'Registered Successfully')
            return redirect('login')
        else:
            messages.success(request,'Password are not matching,Please Try Again')
    return render(request,'signup.html')


def search_student(request):
    student = ""
    searched = ""
    if request.method == "POST":
        try:
            n = request.POST['name']
            searched = n
            student  = Student.objects.get(first_name__icontains=n)
        except:
            try:
                n = request.POST['name']
                searched = n
                student = Student.objects.get(roll_no=n)
            except:
                n = request.POST['name']
                searched = n
                messages.success(request,'Provide accurate name or Roll No')
    d = {'student':student,'searched':searched}
    return render(request,'search_student.html',d)

@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def Logout(request):
    logout(request)
    messages.success(request,'You have Logged out.')
    return redirect('home')


@login_required(login_url='login')
@allowed_users(allowed_roles=['teacher'])
def delete_student(request,pid):
    student = Student.objects.get(id=pid)
    student.delete()
    messages.success(request,'1 data deleted Successfully.')
    return redirect('view_student')