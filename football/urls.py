from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('pages/club-staff.html', views.club_staff_view, name='club_staff_page'),
    



]
