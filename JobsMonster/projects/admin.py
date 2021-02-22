from django.contrib import admin
from .models import Project, ProjectManpowers, Update
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectManpowers)
admin.site.register(Update)


