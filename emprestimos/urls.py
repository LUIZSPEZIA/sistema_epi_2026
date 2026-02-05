from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.listar_emprestimos, name='listar_emprestimos'),
    path('novo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('<int:id>/devolver/', views.devolver_epi, name='devolver_epi'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

]
