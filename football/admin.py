from django.contrib import admin
from .models import CoachingStaff, Player, Club, OtherStaff
from .models import Team, Fixture, Result, Match, Stadium
from .models import Blog
from .models import BlogPost, Highlight





# Register your models here.
admin.site.register(CoachingStaff)
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Stadium)
admin.site.register(Result)
admin.site.register(OtherStaff)
admin.site.register(Highlight)



admin.site.site_header = 'LigiOpen Administration'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('headline', 'description', 'image')
    search_fields = ('headline', 'description')


@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'competition', 'venue', 'team_a_name', 'team_b_name')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ('title', 'author', 'content')
