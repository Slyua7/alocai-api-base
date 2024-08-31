from django.urls import path
from . import views

urlpatterns = [
    path('agendamento/', views.AgendamentoCreateListView.as_view(), name='agendamento-create-list'),
    path('agendamento/<int:pk>/', views.AgendamentoRetrieveUpdateDestroyView.as_view(), name='agendamento-detail-view')
]