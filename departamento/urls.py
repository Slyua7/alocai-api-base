from django.urls import path
from . import views

urlpatterns = [
    path('departamento/', views.DepartamentoCreateListView.as_view(), name='departamento-create-list'),
    path('departamento/<int:pk>/', views.DepartamentoRetrieveUpdateDestroyView.as_view(), name='departamento-detail-view')
]