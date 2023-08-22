from django.urls import path

from . import views

urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login'),
    path('signup', views.UserSignUpView.as_view(), name='signup'),
]