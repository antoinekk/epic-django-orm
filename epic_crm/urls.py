from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('client', ClientView.as_view()),
    path('client/<int:id>', ClientDetailsView.as_view()),
    path('client/<int:id>/contracts', ContractView.as_view()),
    path('contracts/<int:id>', ContractDetailsView.as_view()),
    path('contracts/<int:id>/events', EventView.as_view()),
    path('events/<int:id>', EventDetailsView.as_view())
]