from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('auth_api.urls')),

    path('api/v1/', include('agendamento.urls')),

    path('api/v1/', include('departamento.urls')),

    path('api/v1/', include('predio.urls')),

    path('api/v1/', include('sala.urls')),

    path('api/v1/', include('usuario.urls'))
]
