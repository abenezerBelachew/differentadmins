from django.conf import settings
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Advice, Grade, Subject

from accounts.admin import LogEntryAdmin


class GradeAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "grade"]
    list_filter = ["subject", "grade", "student"]
    list_editable = ["grade"]

class AdviceAdmin(admin.ModelAdmin):
    list_display = ["student", "advice"]
    list_filter = ["student",]
    list_editable = ["advice",]

class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

admin.site.register(Grade, GradeAdmin)
admin.site.register(Advice, AdviceAdmin)
admin.site.register(Subject, SubjectAdmin)