from django.contrib import admin
from .models import Project, Activity, Resource, TeamMember, ProjectManager


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_date', 'end_date', 'description')
    search_fields = ('name', 'location', 'start_date', 'end_date', 'description')
    ordering = ('name', 'location', 'start_date', 'end_date', 'description')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'project', 'description')
    search_fields = ('name', 'start_date', 'end_date', 'project', 'description')
    ordering = ('name', 'start_date', 'end_date', 'project', 'description')
       

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project')
    search_fields = ('name', 'description', 'project')
    ordering = ('name', 'description', 'project')


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project')
    search_fields = ('name', 'description', 'project')
    ordering = ('name', 'description', 'project')


class ProjectManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project')
    search_fields = ('name', 'description', 'project')
    ordering = ('name', 'description', 'project')

# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(ProjectManager, ProjectManagerAdmin)




