from django.contrib import admin
from .models import Task, TaskImages
from django.db.models import Case, When, IntegerField

# Register your models here.
class TaskImagesAdmin(admin.TabularInline):
    model = TaskImages

class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskImagesAdmin,]
    list_display = ('title', 'due_date', 'priority', 'user', 'is_complete')
    list_filter = ('creation_date', 'due_date', 'priority', 'is_complete')
    search_fields = ('title',)
    ordering = (Case(
        When(priority='High', then=1),
        When(priority='Medium', then=2),
        When(priority='Low', then=3),
        default=4,
        output_field=IntegerField(),
    ),)
admin.site.site_header = 'Task Manager Admin'

admin.site.register(Task, TaskAdmin)

