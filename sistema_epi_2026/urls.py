
from django.contrib import admin
from django.urls import path, include
from colaboradores.views import HomeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("colaboradores/", include("colaboradores.urls")),
    path("api/", include("colaboradores.api_urls")),
    # Home: renderiza template simples em vez de redirecionar
    path("", HomeView.as_view(), name='home'),
    path('epi/', include('epi.urls')),
    path('emprestimos/', include('emprestimos.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/restrito/', auth_views.LoginView.as_view(template_name='registration/restrito.html'), name='restrito')
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
