from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='user-create'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='user-detail-view')
]