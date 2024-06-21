from django.urls import path
from . import views
from .views import player_stats_view
# from .views import fixtures_view 
from .views import contact_us_view, success_view
from .views import fixtures_and_results









urlpatterns = [
    path('', views.home, name='home'),

    path('fixtures', views.fixtures_view, name='fixtures'),
    path('pages/club-staff.html', views.club_staff_view, name='club_staff_page'),
    path('player-stats', views.player_stats_view, name='player_stats'),
    path('pages/success.html', views.success_view, name='success'),
    path('contact', views.contact_us_view, name='contact_us'),
    path('contact/success', views.success_view, name='success'),
    path('club', views.club_list_view, name='club_list'),
    path('club/<int:club_id>', views.club_detail_view, name='club_detail'),
    path('fixtures-results/', fixtures_and_results, name='fixtures_results'),

    
]


