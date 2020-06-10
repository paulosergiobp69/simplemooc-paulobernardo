from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.dashboard, name='accounts.dashboard'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="accounts.login"),
    path('sair/', LogoutView.as_view(next_page='core.home'), name="accounts.logout"),
    path('cadastre-se/', views.register, name='accounts.register'),
    path('nova-senha/', views.password_reset, name='accounts.password_reset'),
    path('confirmar-nova-senha/?P<key>/', views.password_reset_confirm, name='accounts.password_reset_confirm'),
    path('editar/', views.edit, name='accounts.edit'),
    path('editar_senha/', views.edit_password, name='accounts.edit_password'),

]
