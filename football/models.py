from django.db import models

# Create your models here.
# League standings table

class LeagueStanding(models.Model):
    position = models.IntegerField()
    team = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_for = models.IntegerField()
    goals_against = models.IntegerField()
    goal_difference = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f'{self.position}. {self.team}'



# Model for Coaching Staff
class CoachingStaff(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='coaching_staff_images/')
    # Add more fields as needed

# Model for Players
class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    club_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True)

# Model for Other Staff
class OtherStaff(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='other_staff_images/')
    # Add more fields as needed



class BaseItem(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Team(BaseItem):
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)

class Venue(BaseItem):
    pass

class Fixture(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_fixtures', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_fixtures', on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} at {self.venue.name} on {self.date}"

    class Meta:
        ordering = ['date', 'time']


