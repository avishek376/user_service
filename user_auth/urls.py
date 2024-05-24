from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UserProfileViewSet

router = routers.DefaultRouter()
router.register("users/",UserProfileViewSet)

urlpatterns = [
    path('registration/', views.AccountRegistration.as_view(),name="registration"),
    path('login/', views.AccountLogin.as_view(),name="login"),
    path('', include(router.urls)),
]