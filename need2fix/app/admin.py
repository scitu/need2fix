from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from app.models import Task

base_exclude = ['id']
class TaskAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Task._meta.fields]
    # list_editable = [f.name for f in Task._meta.fields \
    #     if f.name not in base_exclude]
admin.site.register(Task, TaskAdmin)