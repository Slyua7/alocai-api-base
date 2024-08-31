from django.urls import path
from . import views

urlpatterns = [
    path('professor/', views.ProfessorCreateListView.as_view(), name='professor-create-list'),
    path('professor/<int:pk>/', views.ProfessorRetrieveUpdateDestroyView.as_view(), name='professor-detail-view')
]