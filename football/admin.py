from django.contrib import admin
from .models import Staff, Player, Club, Staff
from .models import Team, FixtureResult, Fixture, Match, Stadium
from .models import Blog
from .models import BlogPost





# Register your models here.
admin.site.register(Staff)
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Stadium)





admin.site.site_header = 'LigiOpen Administration'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('headline', 'description', 'image')
    search_fields = ('headline', 'description')

@admin.register(FixtureResult)
class FixtureResultAdmin(admin.ModelAdmin):
    list_display = (
        'fixture',
        'score',
        'minute'
    )
    search_fields = ('fixture__team_a_name', 'fixture__team_b_name')
    list_filter = ('fixture__date',)

@admin.register(Fixture)
class FixtureAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'time',
        'competition',
        'venue',
        'team_a_name',
        'team_b_name'
    )
    search_fields = ('team_a_name', 'team_b_name', 'competition')
    list_filter = ('date', 'competition')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ('title', 'author', 'content')
