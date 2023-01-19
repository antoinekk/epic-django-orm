from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('client', ClientView.as_view()),
    path('client/<int:id>', ClientDetailsView.as_view())
]