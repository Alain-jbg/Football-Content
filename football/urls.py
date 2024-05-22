from django.urls import path
from . import views
from .views import player_stats_view





urlpatterns = [
    path('', views.home, name='home'),
    path('pages/club-staff.html', views.club_staff_view, name='club_staff_page'),
    path('player-stats/', player_stats_view, name='player_stats'),

    



]
