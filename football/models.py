from django.db import models
from django.utils import timezone
import datetime

# Models

class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='Default Location')
    established_date = models.DateField(default=timezone.now)  
    stadium = models.CharField(max_length=100, default='Default Stadium')
    photo = models.ImageField(upload_to='club_photos/', default='default.jpg') 
    coach_name = models.CharField(max_length=100)
    

    
    def __str__(self):
        return self.name
class Player(models.Model):
    name = models.CharField(max_length=100)
    height_cm = models.PositiveIntegerField(null=True, blank=True)  
    weight_kg = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(default=datetime.date(2000, 1, 1))  
    nationality = models.CharField(max_length=50, default='Unknown')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players', default=1)  
    team = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='photos/players/', default='photos/players/default.jpg')  

def __str__(self):
        return self.name


class CoachingStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Coach')
    nationality = models.CharField(max_length=100, default='Unknown')
    experience = models.CharField(max_length=50, default='1 years')
    club = models.ForeignKey(Club, related_name='coaching_staff', on_delete=models.CASCADE)  
    photo = models.ImageField(upload_to='photos/staff/', default='photos/staff/default.jpg')
    
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    coach = models.CharField(max_length=100, blank=True, null=True)
    home_ground = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)


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
    # scores=models.CharField(max_length=255, default="Team")
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
    date = models.DateField()
    competition = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.opponent} at {self.venue}"

class ResultMatch(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    team_a_score = models.IntegerField()
    team_b_score = models.IntegerField()

    def __str__(self):
        return f"{self.fixture} - {self.team_a_score} vs {self.team_b_score}"