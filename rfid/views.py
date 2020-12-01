from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import AttendanceSerializer
from django.utils import timezone

@api_view(['GET'])
def attendanceList(request):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def attendanceDetail(request, pk):
    attendance = Attendance.objects.get(id=pk)
    serializer = AttendanceSerializer(attendance, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def attendanceCreate(request):
    serializer = AttendanceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def attendanceUpdate(request):

    pk = request.data.get("watch_tag")

    watch_list = Watch.objects.all()
    for watch in watch_list:
        
        if watch.tag == pk:

            obj = Attendance.objects.latest('id')
            if obj.time_out == None:
                if obj.status == False:
                    obj.watch_tag = watch.tag
                    obj.status = True
                    obj.save(update_fields=['watch_tag','status'])
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    obj = Attendance.objects.filter(watch_tag=watch.tag).order_by('-id')[0]
                    obj.time_out = timezone.now()
                    obj.status = False
                    obj.save()
                    return Response(status=status.HTTP_201_CREATED)

    
    student = Student.objects.get(tag=pk)
    log = Attendance.objects.create(
        student_tag =  student,
        name = student.name,
        )
    log.save()
    return Response(status=status.HTTP_201_CREATED)

    