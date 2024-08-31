from django.urls import path
from . import views

urlpatterns = [
    path('auditorio/', views.AuditorioCreateListView.as_view(), name='auditorio-create-list'),
    path('auditorio/<int:pk>/', views.AuditorioRetrieveUpdateDestroyView.as_view(), name='auditorio-detail-view')
]