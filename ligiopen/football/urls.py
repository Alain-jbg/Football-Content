from django.urls import path

from .views import index_view
from . import views

urlpatterns = [
    path('', index_view, name='index'),
    path('pages/login.html/', views.login_view, name='login'),
    path('pages/signup.html/', views.signup_view, name='signup'),

   
 
]

