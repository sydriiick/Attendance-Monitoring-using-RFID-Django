from django.contrib import admin
from .models import *
# Register your models here.


admin.site.site_header = "Attendance Admin"
admin.site.site_title ="Attendance Admin Area"
admin.site.index_title ="Welcome to Attendance Admin Area"



class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','tag','date']
    search_fields = ['name','tag','date']

class WatchAdmin(admin.ModelAdmin):
    list_display = ['tag','date']
    search_fields = ['tag','date']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['name','student_tag','watch_tag','time_in','time_out','status']
    search_fields = ['name','student_tag','watch_tag','time_in','time_out']


admin.site.register(Student, StudentAdmin)
admin.site.register(Watch, WatchAdmin)
admin.site.register(Attendance, AttendanceAdmin)