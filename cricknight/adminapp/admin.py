from django.contrib import admin
from .models.ground  import Ground
from .models.team import Team
from .models.player import Player
from .models.user import User
from .models.batter import BatterModel
from .models.bowler import Bowler
from .models.scorecard import Scorecard
from .models.tournament import Tournament
from .models.match import  Match


class AdminGround(admin.ModelAdmin):
    list_display = ['ground_name', 'ground_id', 'price', 'location','available','timestamp','image']

class AdminUser(admin.ModelAdmin):
    list_display = [ 'firstname', 'lastname','username', 'email','password','contact']

class AdminPlayer(admin.ModelAdmin):
    list_display = [ 'name','age','height','weight']

class AdminTeam(admin.ModelAdmin):
    list_display = ['team_name', 'team_id', 'captain_name']


admin.site.register(Ground,AdminGround)
admin.site.register(Team,AdminTeam)
admin.site.register(Player,AdminPlayer)
admin.site.register(User,AdminUser)
admin.site.register(BatterModel)
admin.site.register(Bowler)
admin.site.register(Scorecard)
admin.site.register(Match)
admin.site.register(Tournament)
