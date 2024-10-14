from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer

from workshopApi.api.serializers import *


@api_view(["GET"])
@renderer_classes([TemplateHTMLRenderer])
def show_doc(request):
    template = loader.get_template("doc.html")
    return HttpResponse(template.render({}, request))


@api_view(["GET"])
@renderer_classes([TemplateHTMLRenderer])
def userManagement(request):
    template = loader.get_template("manageUser.html")
    return HttpResponse(template.render({}, request))


@api_view(["POST"])
def create_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        response = {
            "status": status.HTTP_201_CREATED,
            "data": serializer.data,
            "message": "User created successfully",
        }
        return JsonResponse(response)
    else:
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_user(request, id):
    user = get_object_or_404(CustomUser, id=id)
    user_serialized = UserSerializer(user)
    return JsonResponse(user_serialized.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_fruit(request):
    serializer = FruitSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_fruit(request, name):
    fruit = get_object_or_404(Fruit, name=name)
    fruit_serialized = FruitSerializer(fruit)
    return JsonResponse(fruit_serialized.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_fruit(request, name):
    fruit = get_object_or_404(Fruit, name=name)
    if fruit is not None:
        fruit.delete()
        return JsonResponse("Fruit got deleted", status=status.HTTP_204_NO_CONTENT)
    return JsonResponse("Fruit not found", status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def update_fruit(request, name):
    fruit = get_object_or_404(Fruit, name=name)
    if fruit is not None:
        serializer = FruitSerializer(fruit, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse("Fruit not found", status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def get_fruits(request):
    fruits = Fruit.objects.all()
    fruit_serialized = FruitSerializer(fruits, many=True)
    return JsonResponse(fruit_serialized.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_color(request):
    serializer = ColorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_color(request, name):
    color = get_object_or_404(Color, name=name)
    color_serialized = ColorSerializer(color)
    return JsonResponse(color_serialized.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_color(request, name):
    color = get_object_or_404(Color, name=name)
    if color is not None:
        color.delete()
        return JsonResponse("Color got deleted", status=status.HTTP_204_NO_CONTENT)
    return JsonResponse("Color not found", status=status.HTTP_404_NOT_FOUND)


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


@api_view(["GET"])
def get_colors(request):
    colors = Color.objects.all()
    colors_serialized = ColorSerializer(colors, many=True)
    return JsonResponse(colors_serialized.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_season(request):
    serializer = SeasonSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_season(request, name):
    season = get_object_or_404(Season, name=name)
    season_serialized = SeasonSerializer(season)
    return JsonResponse(season_serialized.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_season(request, name):
    season = get_object_or_404(Season, name=name)
    if season is not None:
        season.delete()
        return JsonResponse("Season got deleted", status=status.HTTP_204_NO_CONTENT)
    return JsonResponse("Season not found", status=status.HTTP_404_NOT_FOUND)


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


@api_view(["GET"])
def get_seasons(request):
    seasons = Season.objects.all()
    seasons_serialized = SeasonSerializer(seasons, many=True)
    return JsonResponse(seasons_serialized.data, status=status.HTTP_200_OK)
