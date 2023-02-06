"""epic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from epic_crm.views import *

router = DefaultRouter()

router.register(r"signup", SignupViewset, basename="signup")
router.register(r"users", UserViewset, basename="user")
router.register(r"clients", ClientViewset, basename="client")

contract_router = NestedDefaultRouter(router, r"clients", lookup="client")
contract_router.register(r"contracts", ContractViewset, basename="contract")
event_router = NestedDefaultRouter(contract_router, r"contracts", lookup="contract")
event_router.register(r"events", EventViewset, basename="event")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/', include(router.urls)),
    path('api/', include(contract_router.urls)),
    path('api/', include(event_router.urls))
]