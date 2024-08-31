from django.urls import path
from . import views

urlpatterns = [
    path('predio_dep/', views.PredioDepCreateListView.as_view(), name='predio_dep-create-list'),
    path('predio_dep/<int:pk>/', views.PredioDepRetrieveUpdateDestroyView.as_view(), name='predio_dep-detail-view')
]