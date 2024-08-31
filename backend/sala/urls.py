from django.urls import path
from . import views

urlpatterns = [
    path('sala/', views.SalaCreateListView.as_view(), name='sala-create-list'),
    path('sala/<int:pk>/', views.SalaRetrieveUpdateDestroyView.as_view(), name='sala-detail-view')
]