from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff, Player, Club, FixtureResult, Fixture
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse
from .models import Match
from .models import Blog
from .models import BlogPost
from .models import Club






def home(request):
    clubs = Club.objects.all()
    fixtures = Fixture.objects.all()

    fixtures_results = FixtureResult.objects.all()
    matches = Match.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'clubs': clubs, 'fixtures_results': fixtures_results,'fixtures': fixtures,'matches': matches,'blogs':blogs})


def club_staff_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    coaching_staff = Staff.objects.filter(club=club, staff_type='Coaching Staff')
    other_staff = Staff.objects.filter(club=club, staff_type='Other Staff')
    club_match_staff = Staff.objects.filter(club=club, staff_type='Club Match Staff')
    players = Player.objects.filter(club=club)
    
    context = {
        'club': club,
        'coaching_staff': coaching_staff,
        'other_staff': other_staff,
        'club_match_staff': club_match_staff,
        'players': players,
    }
    
    return render(request, 'pages/club-staff.html', context)
    
    
def player_detail_view(request, slug):
     club = get_object_or_404(Club, slug=slug)
     players = Player.objects.filter(club=club)

     context = {
         'club': club,
         'players': players,
     }
     
     return render(request, 'pages/club-staff.html', context)


def player_stats_view(request):
    stats = Stat.objects.all()
    players = Player.objects.all()

    return render(request, 'club-staff.html', {'stats': stats,'players':player})



def fixtures_view(request):
    fixtures = Fixture.objects.all()
    return render(request, 'index.html', {'fixtures': fixtures})


def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            issue = form.cleaned_data['issue']

            # Send email
            try:
                send_mail(
                    subject=f'Message from {name}',
                    message=issue,
                    from_email=email,
                    recipient_list=['akothdorothy@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                success_url = reverse('success') + f'?email={email}'
                return redirect(success_url)
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
                return redirect('contact_us')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


def success_view(request):
    email = request.GET.get('email', '')  # Default value if email is not provided
    return render(request, 'pages/success.html', {'email': email})

def results_view(request):
    results = Result.objects.all()
    return render(request, 'pages/club-staff.html', {'results': results})


def club_list_view(request):
    clubs = Club.objects.all()
    return render(request, 'index.html', {'clubs': clubs})


def club_detail_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    players = club.players.all()
    fixtures = club.fixtures.all()
    results = Result.objects.filter(fixture__club=club)

     
    
    return render(request, 'pages/club-staff.html', {'club': club, 'players': players,'fixtures':fixtures,'results':results})



def all_players_view(request):
    players = Player.objects.all()  # Fetch all players from the database
    return render(request, 'pages/all-players.html', {'players': players})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'pages/all-players.html', {'players': players})



def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'pages/blog.html', {'blog_posts': blog_posts})



def highlight_list(request):
    highlights = Highlight.objects.all()
    return render(request, 'index.html', {'highlights': highlights})


def matchday_highlights(request):
    fixtures = Fixture.objects.all()
    for fixture in fixtures:
        fixture.home_goals = fixture.goals.filter(team='home')
        fixture.away_goals = fixture.goals.filter(team='away')
    return render(request, 'pages/match-report.html', {'fixtures': fixtures})



def match_report(request):
    fixtures = Fixture.objects.all()
    return render(request, 'pages/match-report.html', {'fixtures': fixtures})






#FAQ Section views
def faq_page(request):
    return render(request, 'pages/FAQ/faq.html')

def website_page(request):
    return render(request, 'pages/FAQ/website.html')

def about_us_page(request):
    return render(request, 'pages/FAQ/about-us.html')

def financial_page(request):
    return render(request, 'pages/FAQ/financial.html')

def tickets_page(request):
    return render(request, 'pages/FAQ/tickets.html')

def support_page(request):
    return render(request, 'pages/FAQ/support.html')

def data_privacy_page(request):
    return render(request, 'pages/FAQ/data-privacy.html')

def clubs_page(request):
    return render(request, 'pages/FAQ/clubs.html')
    
    #Open Finance views
def finance_about(request):
    return render(request, 'pages/finance/about.html')

def finance_payment_type(request):
    return render(request, 'pages/finance/payment-type.html')

def finance_sponsor(request):
    return render(request, 'pages/finance/sponsor.html')

def crowdfund_pay(request):
    return render(request, 'pages/finance/crowdfund-pay.html')

def mpesa_donate(request):
    return render(request, 'pages/finance/mpesa-donate.html')

def other_donate(request):
    return render(request, 'pages/finance/donate.html')

def crowdfund_mpesa(request):
    return render(request, 'pages/finance/mpesa-pay.html')

def crowdfund_other(request):
    return render(request, 'pages/finance/crowdfund-card.html')


def all_players(request):
    return render(request, 'pages/all-players.html')

def matchday_highlights(request):
    return render(request, 'pages/match-report.html')

def blog(request):
    return render(request, 'pages/blog.html')