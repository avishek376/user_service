from django.urls import path, include
from . import views
from rest_framework import routers
from .views import UserProfileViewSet

router = routers.DefaultRouter()
router.register(r"users",UserProfileViewSet)

urlpatterns = [
    path('registration/', views.UserAccountRegistrationView.as_view(),name="registration"),
    path('login/', views.UserAccountLoginView.as_view(),name="login"),
    path('password-change/', views.UserChangePasswordView.as_view(), name='password_reset'),
    path('password-rest/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('', include(router.urls)),
]