from django.shortcuts import render, redirect, get_object_or_404
from .models import CoachingStaff, Player,Club
from django.contrib.auth import authenticate, login
from .models import Player
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.conf import settings
from .forms import ContactForm


# Create your views here.

def home(request):
    return render(request, 'index.html')
    
def club_staff_view(request):
    return render(request, 'pages/club-staff.html')


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
    players = Player.objects.all()
    return render(request, 'club-staff.html', {'players': players})

def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', '') 
            message = form.cleaned_data['message']

            # Send email
            subject = 'Contact Form Submission'
            sender_email = ''  
            recipient_email = '' 
            email_message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'

            try:
                send_mail(subject, email_message, sender_email, [recipient_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found. Please contact us through other means.')
            except Exception as e:
                return HttpResponse(f'An error occurred: {e}')

            return HttpResponse('Thank you for contacting us!')
        else:
            return HttpResponse('Invalid form data. Please check your inputs and try again.')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
