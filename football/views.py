from django.shortcuts import render, redirect, get_object_or_404
from .models import LeagueStanding
from .models import CoachingStaff, Player, OtherStaff
from django.contrib.auth import authenticate, login
from .models import Fixture
from .forms import FixtureForm
from .models import Player
 



# Create your views here.

def home(request):
    return render(request, 'index.html')

def dashboard_view(request):
    standings = LeagueStanding.objects.all()
    return render(request, 'dashboard.html', {'standings': standings})

def contact_us_view(request):
  return render(request, 'pages/contactus.html') 


def club_staff_view(request):
    return render(request, 'pages/club-staff.html')

def club_staff_view(request):
    coaching_staff = CoachingStaff.objects.all()
    players = Player.objects.all()
    other_staff = OtherStaff.objects.all()
    context = {
        'coaching_staff': coaching_staff,
        'players': players,
        'other_staff': other_staff,
    }
    return render(request, 'pages/club-staff.html', context)


def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_created')
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})

def create_season(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('season_created')
    else:
        form = SeasonForm()
    return render(request, 'create_season.html', {'form': form})
# views.py


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
        else:
            # Handle invalid login
            return render(request, 'pages/login.html', {'error': 'Invalid credentials'})  # Add error message to display on the login page
    else:
        return render(request, 'pages/login.html')  # Render the login form

def admin_dashboard_view(request):
    # Logic for displaying the admin dashboard
    return render(request, 'pages/dashboard.html')  # Render the dashboard template

def dashboard_view(request):
    # Your view logic goes here
    return render(request, 'dashboard.html')




def dashboard_view(request):
    players = Player.objects.all()
    return render(request, 'dashboard.html', {'players': players})

def add_player(request):
    if request.method == 'POST':
        # Process form data and save new player
        # Example: player = Player.objects.create(name=request.POST['name'], ...)
        return redirect('dashboard')  # Redirect to dashboard after adding player
    return render(request, 'add_player.html')

def edit_player(request, player_id):
    player = Player.objects.get(id=player_id)
    if request.method == 'POST':
        # Process form data and update player
        # Example: player.name = request.POST['name'], player.save()
        return redirect('dashboard')  # Redirect to dashboard after editing player
    return render(request, 'edit_player.html', {'player': player})


# views.py in your app


def index(request):
    clubs = Club.objects.all()
    return render(request, 'index.html', {'clubs': clubs})

def add_club(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        club = Club.objects.create(name=name, logo=logo)
        return redirect('index')
    return render(request, 'add_club.html')

def delete_club(request, club_id):
    club = Club.objects.get(pk=club_id)
    club.delete()
    return redirect('index')

def update_club(request, club_id):
    club = Club.objects.get(pk=club_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        club.name = name
        club.logo = logo
        club.save()
        return redirect('index')
    return render(request, 'update_club.html', {'club': club})
