from django.contrib import admin

# Register your models here.
from .models import  (Course, Enrollment, Announcement, Comment, Lesson, Material)

class CourseAdmin(admin.ModelAdmin):
    # campos a serem apresentados no grid cursos
    list_display = ['name', 'slug', 'start_date', 'created_at'] 
    # campos definidos para buscas na acao pesquisar tela de cursos
    search_fields = ['name', 'slug'] 
    # adicionado - para o campo slug automaticamente, nao esquecer da virgula apos o ultimo campo
    prepopulated_fields = {'slug':('name',)} 


#class MaterialInlineAdmin(admin.TabularInline):
class MaterialInlineAdmin(admin.StackedInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [
        MaterialInlineAdmin
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material]) 
admin.site.register(Lesson, LessonAdmin)

