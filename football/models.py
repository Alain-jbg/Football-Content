from django.db import models
from django.utils import timezone

def upload_to(instance, filename):
    """Generate dynamic upload paths based on instance and file type."""
    upload_paths = {
        Club: 'club_photos/',
        Player: 'players/',
        Staff: 'staff/',
        Team: 'team_logos/',
        FixtureResult: 'team_logos/',
        Match: 'match_logos/',
        Blog: 'blog_images/',
        BlogPost: 'blogpost_images/',
        ClubMatch: 'club_logos/',
    }
    return upload_paths.get(type(instance), '') + filename

class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    established_date = models.DateField(default=timezone.now)
    stadium = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    coach_name = models.CharField(max_length=100, blank=True, null=True)
    coach_photo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)
    height_cm = models.PositiveIntegerField(blank=True, null=True)
    weight_kg = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(default=timezone.now)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    team = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    apps = models.IntegerField()
    mins = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    motm = models.IntegerField()

    RATING_CHOICES = [
        ('⭐', '1 Star'),
        ('⭐⭐', '2 Stars'),
        ('⭐⭐⭐', '3 Stars'),
        ('⭐⭐⭐⭐', '4 Stars'),
        ('⭐⭐⭐⭐⭐', '5 Stars'),
    ]

    rating = models.CharField(
        max_length=6,
        choices=RATING_CHOICES,
        blank=True,
        null=True,
        help_text="Emoji rating (e.g., ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐)"
    )

    def __str__(self):
        return self.name



class Staff(models.Model):
    STAFF_ROLES = [
        ('Coaching Staff', 'Coaching Staff'),
        ('Other Staff', 'Other Staff'),
        ('Club Match Staff', 'Club Match Staff'),
    ]

    ROLE_CHOICES = [
        ('Head Coach', 'Head Coach'),
        ('Assistant Coach', 'Assistant Coach'),
        ('Physiotherapist', 'Physiotherapist'),
        ('Team Manager', 'Team Manager'),
        ('Scout', 'Scout'),
    ]
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    staff_type = models.CharField(max_length=100, choices=STAFF_ROLES)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=50, blank=True, null=True)
    club = models.ForeignKey(Club, related_name='staff', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.staff_type})"

class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    coach = models.CharField(max_length=100, blank=True, null=True)
    home_ground = models.CharField(max_length=100, blank=True, null=True)
    lineup = models.TextField(blank=True, null=True)
    substitutes = models.TextField(blank=True, null=True)
    booked = models.CharField(max_length=255, blank=True, null=True)
    goalscorers = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# class Result(models.Model):
#     score = models.CharField(max_length=100, blank=True, null=True)
#     minute = models.IntegerField(default=0)
#     is_home_team = models.BooleanField(default=True)
#     fixture = models.ForeignKey('Fixture', related_name='results', on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to=upload_to, blank=True, null=True)

#     def __str__(self):
#         return f"{self.score} - {self.minute} min"


class Fixture(models.Model):
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    competition = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    team_a_name = models.CharField(max_length=255)
    team_a_logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    team_b_name = models.CharField(max_length=255)
    team_b_logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return f"{self.team_a_name} vs {self.team_b_name} on {self.date}"


class FixtureResult(models.Model):
    fixture = models.OneToOneField(Fixture, related_name='result', on_delete=models.CASCADE, blank=True, null=True)  # Allow null initially
    score = models.CharField(max_length=20, default=0)
    minute = models.IntegerField(blank=True, null=True)
    result_photo = models.ImageField(upload_to='result_photos/', blank=True, null=True)

    def __str__(self):
        if self.fixture:  
         return f"Result: {self.fixture.team_a_name} vs {self.fixture.team_b_name} on {self.fixture.date} - Score: {self.score or 'No score'}"
        return "Result with no associated fixture"


class Stadium(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    date_time = models.DateTimeField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Club, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Club, related_name='away_matches', on_delete=models.CASCADE)
    home_team_logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    away_team_logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    first_half_summary = models.TextField(blank=True, null=True)
    second_half_summary = models.TextField(blank=True, null=True)
    referee_name = models.CharField(max_length=100, blank=True, null=True)
    author_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} on {self.date_time.strftime('%B %d, %Y')}"

class Blog(models.Model):
    headline = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.headline


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    day = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    author_image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.title
        
        

class ClubMatch(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.name



