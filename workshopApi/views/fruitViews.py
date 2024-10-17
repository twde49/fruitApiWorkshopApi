from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from workshopApi.api.serializers import *


# view for create a fruit by the api
@login_required
@api_view(["POST"])
def create_fruit(request):
    serializer = FruitSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to get a fruit with it info by the api
@login_required
@api_view(["GET"])
def get_fruit(name):
    fruit = get_object_or_404(Fruit, name=name)
    fruit_serialized = FruitSerializer(fruit)
    return JsonResponse(fruit_serialized.data, status=status.HTTP_200_OK)


# view to delete a fruit by the api
@login_required
@api_view(["DELETE"])
def delete_fruit(name):
    fruit = get_object_or_404(Fruit, name=name)
    if fruit is not None:
        fruit.delete()
        return JsonResponse("Fruit got deleted", status=status.HTTP_204_NO_CONTENT)
    return JsonResponse("Fruit not found", status=status.HTTP_404_NOT_FOUND)


# view to update fruit info from the api
@login_required
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


# view to show all fruits stored in db from api
@login_required
@api_view(["GET"])
def get_fruits():
    fruits = Fruit.objects.all()
    fruit_serialized = FruitSerializer(fruits, many=True)
    return JsonResponse(fruit_serialized.data, status=status.HTTP_200_OK)
