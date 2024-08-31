from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.UsuarioCreateListView.as_view(), name='usuario-create-list'),
    path('usuario/<int:pk>/', views.UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail-view')
]