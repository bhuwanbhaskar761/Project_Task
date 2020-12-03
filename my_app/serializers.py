from rest_framework import serializers
from .models import Teacher,Student

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'