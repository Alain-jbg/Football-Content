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
    path('pages/FAQ/faq', views.faq_page, name='faq_page'),

    # FAQ Section URLs
    path('pages/FAQ/website', views.website_page, name='website_page'),
    path('pages/FAQ/about-us', views.about_us_page, name='about_us_page'),
    path('pages/FAQ/financial', views.financial_page, name='financial_page'),
    path('pages/FAQ/tickets', views.tickets_page, name='tickets_page'),
    path('pages/FAQ/support', views.support_page, name='support_page'),
    path('pages/FAQ/data-privacy', views.data_privacy_page, name='data_privacy_page'),
    path('pages/FAQ/clubs', views.clubs_page, name='clubs_page'),    

    #Open finance URLs
    path('pages/finance/about/', views.finance_about, name='finance-about'),
    path('pages/finance/payment-type/', views.finance_payment_type, name='finance-payment-type'),
    path('pages/finance/sponsor/', views.finance_sponsor, name='finance-sponsor'),
    path('pages/crowdfund-pay/', views.crowdfund_pay, name='crowdfund-pay'),
    path('pages/finance/mpesa-donate', views.mpesa_donate, name='mpesa_donate'),
    path('pages/finance/other-donate', views.other_donate, name='other_donate'),
    path('pages/finance/crowdfund-mpesa', views.crowdfund_mpesa, name='crowdfund_mpesa'),
    path('pages/finance/crowdfund-other', views.crowdfund_other, name='crowdfund_other')
    # ... other URL patterns ...
]


