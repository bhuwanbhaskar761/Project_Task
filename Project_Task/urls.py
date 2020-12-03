"""Project_Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/',teacherList.as_view()),
    path('student/',studentList.as_view()),
    path('add_student/',add_student,name='add_student'),
    path('',home,name='home'),
    path('teacher_home',teacher_home,name='teacher_home'),
    path('search_student',search_student,name='search_student'),
    path('view_student/',view_student,name="view_student"),
    path('login/',Login_User,name="login"),
    path('signup/',signup,name="signup"),
    path('logout/',Logout,name="logout"),
    path('delete_student/<int:pid>/',delete_student,name="delete_student"),
    path('edit_student/<int:pid>/',edit_student,name="edit_student"),
]
