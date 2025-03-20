from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
<<<<<<< HEAD
from .models import Leaderboard , Player, Winner
from .serializers import LeaderboardSerializer, PlayerSerializer, WinnerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView

# code to add player to leaderboard
=======
from .models import Leaderboard , Player
from .serializers import LeaderboardSerializer, PlayerSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

>>>>>>> b4c5730e8052513033a436a361ad9e1c103f2052
@csrf_exempt
@api_view(['GET', 'POST'])
def leaderboard_list(request):
    if request.method == 'GET':
        players = Leaderboard.objects.all().order_by('time')
        serializer = LeaderboardSerializer(players, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
            serializer = LeaderboardSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
<<<<<<< HEAD

# code to add player in the model    
=======
    
>>>>>>> b4c5730e8052513033a436a361ad9e1c103f2052
@csrf_exempt
@api_view(['GET', 'POST'])
def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all() # Fastest first
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
            serializer = PlayerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
<<<<<<< HEAD


# code to delete or update the data of the model    
@csrf_exempt
@api_view(['PATCH', 'DELETE', 'PUT'])
=======
@csrf_exempt
@api_view(['PATCH', 'DELETE'])
>>>>>>> b4c5730e8052513033a436a361ad9e1c103f2052
def player_detail(request, player_id):
    """Update or delete a specific player."""
    player = get_object_or_404(Player, id=player_id)

    if request.method == 'PATCH':
        serializer = PlayerSerializer(player, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player.delete()
<<<<<<< HEAD
        return Response({"message": "Player deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
# code to add winner
@csrf_exempt
@api_view(['GET', 'POST'])
def winner_list(request):
    if request.method == 'GET':
        players = Winner.objects.all()
        serializer = WinnerSerializer(players, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
            serializer = WinnerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
        return Response({"message": "Player deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
>>>>>>> b4c5730e8052513033a436a361ad9e1c103f2052
