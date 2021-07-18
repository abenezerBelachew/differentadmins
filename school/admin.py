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


class ColoredAdminSite(admin.sites.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context["site_header_color"] = getattr(
            self, "site_header_color", None
        )
        context["module_caption_color"] = getattr(
            self, "module_caption_color", None
        )
        context["fontawesome_icon"] = getattr(
            self, "fontawesome_icon", None
        )
        context["breadcrumb_background_color"] = getattr(
            self, "breadcrumb_background_color", None
        )
        return context

class TeacherAdminSite(ColoredAdminSite):
    if settings.DEBUG == True:
        site_header = "Teacher's Admin [Development]"
    else:
        site_header = "Teacher's Admin"
    site_title = "Teacher's Admin Portal"
    index_title = "Welcome to the Teacher's Admin"
    fontawesome_icon = "fas fa-chalkboard-teacher"
    site_header_color = "gray"
    module_caption_color = "black"
    breadcrumb_background_color = "#a06767"

    def has_permission(self, request):
            return (
            request.user.is_active and request.user.is_teacher
        )

teacher_admin_site = TeacherAdminSite(name="teachers_admin")
teacher_admin_site.register(Grade, GradeAdmin)
teacher_admin_site.register(Advice, AdviceAdmin)

class CounselorsAdminSite(ColoredAdminSite):
    if settings.DEBUG == True:
        site_header = "Counselor's Admin [Development]"
    else:
        site_header = "Counselor's Admin [Prod]"    
    site_title = "Counselor's Admin Portal"
    index_title = "Welcome to the Counselor's Admin"
    site_header_color = "green"
    module_caption_color = "blue"
    fontawesome_icon = "fas fa-people-carry"

    def has_permission(self, request):
        return (
            request.user.is_active and request.user.is_counselor
        )

counselor_admin_site = CounselorsAdminSite(name="counselors_admin")
counselor_admin_site.register(Advice, AdviceAdmin)
counselor_admin_site.register(Grade, GradeAdmin)

class HeadmasterAdminSite(ColoredAdminSite):
    if settings.DEBUG == True:
        site_header = "Headmaster's Admin [Development]"
    else:
        site_header = "Headmaster's Admin"

    site_title = "Headmaster's Admin Portal"
    index_title = "Welcome to the Headmaster's Admin"
    site_header_color = "purple"
    module_caption_color = "blue"
    fontawesome_icon = "fas fa-cash-register"

    def has_permission(self, request):
        return (
            request.user.is_active and request.user.is_headmaster
        )

headmaster_admin_site = HeadmasterAdminSite(name="headmasters_admin")
headmaster_admin_site.register(Grade, GradeAdmin)
headmaster_admin_site.register(Subject, SubjectAdmin)
headmaster_admin_site.register(Advice, AdviceAdmin)
headmaster_admin_site.register(LogEntry, LogEntryAdmin)
