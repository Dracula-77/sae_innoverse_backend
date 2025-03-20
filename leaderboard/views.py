from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Leaderboard, Player, Winner
from .serializers import LeaderboardSerializer, PlayerSerializer, WinnerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

# Class-Based View to handle leaderboard
class leaderboard_list(APIView):
    def get(self, request):
        players = Leaderboard.objects.all().order_by('time')
        serializer = LeaderboardSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Class-Based View to handle players
class player_list(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function-Based View for player detail
@api_view(['PATCH', 'DELETE'])
def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)

    if request.method == 'PATCH':
        serializer = PlayerSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player.delete()
        return Response({"message": "Player deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Function-Based View for winners
@api_view(['GET', 'POST'])
def winner_list(request):
    if request.method == 'GET':
        winners = Winner.objects.all()
        serializer = WinnerSerializer(winners, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WinnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
