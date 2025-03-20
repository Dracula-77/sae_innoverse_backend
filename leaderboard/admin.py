from django.contrib import admin
from .models import Leaderboard
from .models import Player, Winner
# Register your models here.
admin.site.register(Leaderboard)
admin.site.register(Player)
admin.site.register(Winner)
