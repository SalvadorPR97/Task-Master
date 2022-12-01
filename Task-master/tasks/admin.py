from django.contrib import admin

from . import models

class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = "due_date"
    search_fields = ['name', 'due_date']
    list_filter = ['priority', 'due_date']
    list_display = [
        'name',
        'priority',
        'due_date',
        'orden',
        'matraca'
    ]
    
    @admin.display(boolean=True, description='Completadas')
    def matraca(self, instance):
        return instance.finished

admin.site.register(models.Task, TaskAdmin)

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Project, ProjectAdmin)