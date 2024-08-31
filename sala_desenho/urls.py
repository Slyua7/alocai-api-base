from django.urls import path
from . import views

urlpatterns = [
    path('sala_desenho/', views.SalaDesenhoCreateListView.as_view(), name='sala_desenho-create-list'),
    path('sala_desenho/<int:pk>/', views.SalaDesenhoRetrieveUpdateDestroyView.as_view(), name='sala_desenho-detail-view')
]