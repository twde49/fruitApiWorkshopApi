from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from workshopApi.api.serializers import *


# view to create a new color from api
@login_required
@api_view(["POST"])
def create_color(request):
    serializer = ColorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to get color info from the api
@login_required
@api_view(["GET"])
def get_color(name):
    color = get_object_or_404(Color, name=name)
    color_serialized = ColorSerializer(color)
    return JsonResponse(color_serialized.data, status=status.HTTP_200_OK)


# view to remove a color from the api
@login_required
@api_view(["DELETE"])
def delete_color(name):
    color = get_object_or_404(Color, name=name)
    if color is not None:
        color.delete()
        return JsonResponse("Color got deleted", status=status.HTTP_204_NO_CONTENT)
    return JsonResponse("Color not found", status=status.HTTP_404_NOT_FOUND)


# view to update a color data from the api
@login_required
@api_view(["PUT"])
def update_color(request, name):
    color = get_object_or_404(Color, name=name)
    if color is not None:
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse("Color not found", status=status.HTTP_404_NOT_FOUND)


# view to show all colors in db from api
@login_required
@api_view(["GET"])
def get_colors():
    colors = Color.objects.all()
    colors_serialized = ColorSerializer(colors, many=True)
    return JsonResponse(colors_serialized.data, status=status.HTTP_200_OK)
