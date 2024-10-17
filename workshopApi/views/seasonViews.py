from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from workshopApi.api.serializers import *


# view to create a new season from api
@login_required
@api_view(["POST"])
def create_season(request):
    serializer = SeasonSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to get season info from api
@login_required
@api_view(["GET"])
def get_season(name):
    season = get_object_or_404(Season, name=name)
    season_serialized = SeasonSerializer(season)
    return JsonResponse(season_serialized.data, status=status.HTTP_200_OK)


# view to remove a season from api
@login_required
@api_view(["DELETE"])
def delete_season(name):
    season = get_object_or_404(Season, name=name)
    if season is not None:
        season.delete()
        return JsonResponse("Season got deleted", status=status.HTTP_204_NO_CONTENT)
    return JsonResponse("Season not found", status=status.HTTP_404_NOT_FOUND)


# view to update season info from api
@login_required
@api_view(["PUT"])
def update_season(request, name):
    season = get_object_or_404(Season, name=name)
    if season is not None:
        serializer = SeasonSerializer(season, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse("Season not found", status=status.HTTP_404_NOT_FOUND)


# view to show all seasons from the api
@login_required
@api_view(["GET"])
def get_seasons():
    seasons = Season.objects.all()
    seasons_serialized = SeasonSerializer(seasons, many=True)
    return JsonResponse(seasons_serialized.data, status=status.HTTP_200_OK)
