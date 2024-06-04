from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.signupPage, name='signup'),
    path('login', views.loginPage, name='login'),
    path('home', views.homePage, name='home'),
    path('logout', views.logoutPage, name='logout')
]
