from rest_framework import serializers
from .models import Course, Teacher


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'course', 'firstName', 'lastName', 'otch']
