from django.urls import path
from . import views

urlpatterns = [
    path('enderecosusuario/', views.EnderecosUsuarioCreateListView.as_view(), name='enderecosusuario-create-list'),
    path('enderecosusuario/<int:pk>/', views.EnderecosUsuarioRetrieveUpdateDestroyView.as_view(), name='enderecosusuario-detail-view')
]