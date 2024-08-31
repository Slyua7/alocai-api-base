from django.urls import path
from . import views

urlpatterns = [
    path('enderecospredio/', views.EnderecosPredioCreateListView.as_view(), name='enderecospredio-create-list'),
    path('enderecospredio/<int:pk>/', views.EnderecosPredioRetrieveUpdateDestroyView.as_view(), name='enderecospredio-detail-view')
]