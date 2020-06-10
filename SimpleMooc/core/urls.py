from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='core.home'),
    path('contato/',  views.contact, name='core.contact'),
]


#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.home),
#    path('products/', views.products),
#    path('customer/', views.customer),