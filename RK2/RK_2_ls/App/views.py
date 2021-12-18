from rest_framework import viewsets
from .serializers import CourseSerializer, TeacherSerializer
from .models import Course, Teacher
from django.shortcuts import render
from django.http import Http404


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


def CourseList(request):
    return render(request, 'course/list.html', {'c_list': Course.objects.all()})


def TeacherList(request):
    return render(request, 'teacher/list.html', {'t_list': Teacher.objects.all()})


def CourseView(request, course_id):
    try:
        c = Course.objects.get(id=course_id)
    except:
        raise Http404('Курс не найден!')
    return render(request, 'course/detail.html', {'course': c})


def TeacherView(request, teacher_id):
    try:
        t = Teacher.objects.get(id=teacher_id)
    except:
        raise Http404('Преподаватель не найден!')
    return render(request, 'teacher/detail.html', {'teacher': t})
