from django.contrib import admin
from .models import CoachingStaff, Player, Club
from .models import Team, Fixture, Result, FixtureMatch, ResultMatch



# Register your models here.
admin.site.register(CoachingStaff)
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Result)
admin.site.register(ResultMatch)
admin.site.register(FixtureMatch)




@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'competition', 'venue', 'team_a_name', 'team_b_name')


