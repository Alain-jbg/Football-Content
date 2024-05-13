from django.contrib import admin
from .models import LeagueStanding
from .models import CoachingStaff, Player, OtherStaff



# Register your models here.
admin.site.register(LeagueStanding)
admin.site.register(CoachingStaff)
admin.site.register(Player)
admin.site.register(OtherStaff)


