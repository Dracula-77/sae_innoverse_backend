from rest_framework import serializers
from .models import Leaderboard
<<<<<<< HEAD
from .models import Player, Winner
=======
from .models import Player
>>>>>>> b4c5730e8052513033a436a361ad9e1c103f2052
class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = "__all__"

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
<<<<<<< HEAD
        fields = "__all__"
class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = "__all__"
=======
        fields = "__all__"
>>>>>>> b4c5730e8052513033a436a361ad9e1c103f2052
