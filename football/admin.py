from django.contrib import admin
from .models import CoachingStaff, Player, Club, OtherStaff
from .models import Team, Fixture, Result, Match, Stadium



# Register your models here.
admin.site.register(CoachingStaff)
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Stadium)




admin.site.register(Result)
admin.site.register(OtherStaff)



admin.site.site_header = "LigiOpen Admin"




@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'competition', 'venue', 'team_a_name', 'team_b_name')


