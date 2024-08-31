from django.urls import path
from . import views

urlpatterns = [
    path('predio/', views.PredioCreateListView.as_view(), name='predio-create-list'),
    path('predio/<int:pk>/', views.PredioRetrieveUpdateDestroyView.as_view(), name='predio-detail-view')
]