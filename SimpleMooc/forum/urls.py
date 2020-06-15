from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='forum.index'),
    path('tag/<tag>/', views.index, name='forum.index_tagged'),
    path('<slug>/', views.thread, name='forum.thread'),
    path('respostas/<pk>/correta/', views.reply_correct, name='forum.reply_correct'),
    path('respostas/<pk>/incorreta/', views.reply_incorrect, name='forum.reply_incorrect'),
 
]
