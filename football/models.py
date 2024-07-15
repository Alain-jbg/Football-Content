from django.db import models
from django.utils import timezone
import datetime

class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default='')
    established_date = models.DateField(default=timezone.now)
    stadium = models.CharField(max_length=100, default='')
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
    nationality = models.CharField(max_length=50, default='')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    team = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/players/', default='photos/players/default.jpg')
    apps = models.IntegerField(default=0)
    mins = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0, verbose_name='')
    red_cards = models.IntegerField(default=0, verbose_name='')
    motm = models.IntegerField(default=0, verbose_name='')
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name

class OtherStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=100, default='')
    experience = models.CharField(max_length=50, default='')
    club = models.ForeignKey(Club, related_name='other_staff', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/staff/', default='photos/staff/default.jpg')
    
    def __str__(self):
        return self.name

class CoachingStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=100, default='')
    experience = models.CharField(max_length=50, default='')
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
    score = models.CharField(max_length=100, default='')
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
    score = models.CharField(max_length=20, blank=True, null=True)
    team_a_name = models.CharField(max_length=255, default="")
    team_a_logo = models.ImageField(upload_to='team_logos/', null=True)
    team_b_name = models.CharField(max_length=255, default="")
    team_b_logo = models.ImageField(upload_to='team_logos/', null=True)
    
    def __str__(self):
        return f"{self.team_a_name} vs {self.team_b_name} on {self.date}"


class Stadium(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    date_time = models.DateTimeField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Club, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Club, related_name='away_matches', on_delete=models.CASCADE)
    home_team_logo = models.ImageField(upload_to='match_logos/', blank=True, null=True)
    away_team_logo = models.ImageField(upload_to='match_logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} - {self.date_time.strftime('%b %d, %Y | %I:%M %p')}"