from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.AccountRegistration.as_view(),name="registration"),
    path('login/', views.AccountLogin.as_view(),name="login"),
]