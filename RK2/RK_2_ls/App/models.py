from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField('Название курса', max_length=50)


class Teacher(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    firstName = models.CharField('Имя', max_length=50)
    lastName = models.CharField('Фамилия', max_length=50)
    otch = models.CharField('Отчество', max_length=50)

    def fio(self):
        return self.lastName + ' ' + self.firstName + ' ' + self.otch

    def __str__(self):
        return self.fio() + " | Курс: " + self.course.name
