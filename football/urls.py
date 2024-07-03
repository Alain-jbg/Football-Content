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
    path('all-players/', views.all_players_view, name='all_players'),


    
    path('pages/FAQ/faq.html', views.faq_page, name='faq_page'),

    # FAQ Section URLs
    path('pages/FAQ/website.html', views.website_page, name='website_page'),
    path('pages/FAQ/about-us.html', views.about_us_page, name='about_us_page'),
    path('pages/FAQ/financial.html', views.financial_page, name='financial_page'),
    path('pages/FAQ/tickets.html', views.tickets_page, name='tickets_page'),
    path('pages/FAQ/support.html', views.support_page, name='support_page'),
    path('pages/FAQ/data-privacy.html', views.data_privacy_page, name='data_privacy_page'),
    path('pages/FAQ/clubs.html', views.clubs_page, name='clubs_page'),    
]


