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
    
    def __str__(self):
        return self.name
class Player(models.Model):
    name = models.CharField(max_length=100)
    height_cm = models.PositiveIntegerField(null=True, blank=True)  
    weight_kg = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(default=datetime.date(2000, 1, 1))  
    nationality = models.CharField(max_length=50, default='Unknown')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    team = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='photos/players/', default='photos/players/default.jpg')  

def __str__(self):
        return self.name


class CoachingStaff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Coach')
    nationality = models.CharField(max_length=100, default='Unknown')
    experience = models.CharField(max_length=50, default='1 years')
    club = models.CharField(max_length=50, default='Default Club')  
    photo = models.ImageField(upload_to='photos/staff/', default='photos/staff/default.jpg')
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)

    
    
    def __str__(self):
        return self.name



