from django.urls import path
from . import views

urlpatterns = [
    path('laboratorio/', views.LaboratorioCreateListView.as_view(), name='laboratorio-create-list'),
    path('laboratorio/<int:pk>/', views.LaboratorioRetrieveUpdateDestroyView.as_view(), name='laboratorio-detail-view')
]