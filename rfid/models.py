from django.db import models
from datetime import datetime
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    tag  = models.CharField(max_length=15, unique=True, verbose_name='RFID')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return self.tag

class Watch(models.Model):
    tag  = models.CharField(max_length=15, unique=True, verbose_name='RFID')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    def __str__(self):
        return self.tag

class Attendance(models.Model):
    student_tag = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Student RFID')
    watch_tag   = models.CharField(max_length=15, verbose_name='Watch RFID')
    name        = models.CharField(max_length=50, verbose_name='Name')
    status        = models.BooleanField(default=False, verbose_name='Status')
    time_in     = models.DateTimeField(auto_now_add=True, verbose_name='Time-in')
    time_out    = models.DateTimeField(null=True, blank=True, verbose_name='Time-out')

    def __str__(self):
        return str(self.id)