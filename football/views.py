from django.shortcuts import render, redirect, get_object_or_404
from .models import CoachingStaff, Player, Club, Fixture, Result
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse


def home(request):
    clubs = Club.objects.all()
    fixtures = Fixture.objects.all()
    return render(request, 'index.html', {'clubs': clubs, 'fixtures': fixtures})


def club_staff_view(request):
    coaching_staff = CoachingStaff.objects.all()
    players = Player.objects.all()
    context = {
        'coaching_staff': coaching_staff,
        'players': players,
    }
    return render(request, 'pages/club-staff.html', context)


def club_details_view(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    players = Player.objects.filter(club=club)
    return render(request, 'index.html', {'club': club, 'players': players})


def player_detail_view(request, slug):
    club = get_object_or_404(Club, slug=slug)
    players = Player.objects.filter(club=club)
    context = {
        'club': club,
        'players': players
    }
    return render(request, 'pages/club-staff.html', context)


def player_stats_view(request):
    # Assuming Stat model exists, adjust this view accordingly
    stats = Stat.objects.all()
    return render(request, 'club-staff.html', {'stats': stats})


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
                    f'Message from {name}', 
                    issue,  
                    email,  
                    ['wangarraakoth@gmail.com'],  
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
    email = request.GET.get('email')
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

    return render(request, 'pages/club-staff.html', {'club': club, 'players': players})


def fixtures_and_results(request):
    fixtures = Fixture.objects.all()
    results = Result.objects.all()
    return render(request, 'pages/club-staff.html', {
        'fixtures': fixtures,
        'results': results
    })

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