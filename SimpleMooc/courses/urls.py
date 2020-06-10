from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.index, name='courses.index'),
    # passando parametros na url
    #path('cursos/<int:pk>/', views.details, name='courses.details'),
    # utilizando os slugs
    path('cursos/<slug>/', views.details, name='courses.details'),
    path('inscricao/<slug>/', views.enrollment, name='courses.enrollment'),
    path('cancelar-inscricao/<slug>/', views.undo_enrollment, name='courses.undo_enrollment'),
    path('anuncios/<slug>/', views.announcements, name='courses.announcements'),
    path('anuncios/<slug>/<int:pk>/', views.show_announcement, name='courses.show_announcement'),
    path('aulas/<slug>/', views.lessons, name='courses.lessons'),
    path('aulas/<slug>/<int:pk>/', views.lesson, name='courses.lesson'),
    path('materiais/<slug>/<int:pk>/', views.material, name='courses.material'),
    
    #path('(?P<pk>\d+)', views.details, name='courses.details'),


]
