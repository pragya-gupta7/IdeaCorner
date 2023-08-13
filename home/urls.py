from django.contrib import admin
from django.urls import path
from home import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser, name='logout')
]