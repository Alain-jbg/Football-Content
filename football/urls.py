from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    path('pages/contactus.html', views.contact_us_view, name='contact_us'),
    path('pages/club-staff.html', views.club_staff_view, name='club-staff'),
    path('create-team/', views.create_team, name='create_team'),
    path('create-season/', views.create_season, name='create_season'),
    path('pages/login.html/', views.admin_login_view, name='admin_login'),
    path('dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('pages/dashboard.html', views.dashboard_view, name='dashboard'),
    path('add/', views.add_player, name='add_player'),
    path('edit/<int:player_id>/', views.edit_player, name='edit_player'),
    

    




    







]
