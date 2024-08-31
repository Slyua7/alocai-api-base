from django.urls import path
from . import views

urlpatterns = [
    path('coordenador/', views.CoordenadorCreateListView.as_view(), name='coordenador-create-list'),
    path('coordenador/<int:pk>/', views.CoordenadorRetrieveUpdateDestroyView.as_view(), name='coordenador-detail-view')
]