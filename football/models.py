from django.db import models
from django.utils import timezone
import datetime

class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='Default Location')
    established_date = models.DateField(default=timezone.now)
    stadium = models.CharField(max_length=100, default='Default Stadium')
    photo = models.ImageField(upload_to='club_photos/', default='default.jpg')
    coach_name = models.CharField(max_length=100, blank=True, null=True)
    coach_photo = models.ImageField(upload_to='coach_photos/', default='coach_photos/default.jpg')

    
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True)
    height_cm = models.PositiveIntegerField(null=True, blank=True)  
    weight_kg = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(default=datetime.date(2000, 1, 1))
    nationality = models.CharField(max_length=50, default='Unknown')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    team = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/players/', default='photos/players/default.jpg')
    apps = models.IntegerField(default=0)
    mins = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0, verbose_name='Yellow Cards')
    red_cards = models.IntegerField(default=0, verbose_name='Red Cards')
    motm = models.IntegerField(default=0, verbose_name='Man of the Match')
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name

class CoachingStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Coach')
    nationality = models.CharField(max_length=100, default='Unknown')
    experience = models.CharField(max_length=50, default='1 year')
    club = models.ForeignKey(Club, related_name='coaching_staff', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/staff/', default='photos/staff/default.jpg')
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    coach = models.CharField(max_length=100, blank=True, null=True)
    home_ground = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Result(models.Model):
    scorer = models.CharField(max_length=100, default='Unknown Scorer')
    minute = models.IntegerField(default=0)
    is_home_team = models.BooleanField(default=True)
    fixture = models.ForeignKey('Fixture', related_name='goals', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='goal_photos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.scorer} - {self.minute} min"

class Fixture(models.Model):
    date = models.DateField()
    time = models.TimeField(default=datetime.time(12, 0))
    competition = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    team_a_name = models.CharField(max_length=255, default="Team A")
    team_a_logo = models.ImageField(upload_to='team_logos/', null=True)
    team_b_name = models.CharField(max_length=255, default="Team B")
    team_b_logo = models.ImageField(upload_to='team_logos/', null=True)
    
    def __str__(self):
        return f"{self.team_a_name} vs {self.team_b_name} on {self.date}"

class FixtureMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)  # Default value set to None
    date = models.DateField()
    competition = models.CharField(max_length=100)
    team_home = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_fixtures', default=None)
    team_away = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_fixtures', default=None)
    opponent = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.team_home} vs {self.team_away} on {self.date}"


class ResultMatch(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    team_a_score = models.IntegerField()
    team_b_score = models.IntegerField()
    goal_details_home = models.TextField(default='')
    goal_details_away = models.TextField(default='')
    
    def __str__(self):
        return f"{self.fixture} - {self.team_a_score} vs {self.team_b_score}"


