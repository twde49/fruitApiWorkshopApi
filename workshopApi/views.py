from gc import get_objects

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from rest_framework import views, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from workshopApi.api.serializers import *


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def show_doc(request):
        template = loader.get_template('doc.html')
        return HttpResponse(template.render({}, request))

@api_view(['POST'])
def create_user(request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = {
                        'status': status.HTTP_201_CREATED,
                        'data': serializer.data,
                        'message': 'User created successfully'
                }
                return JsonResponse(response)
        else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request,id):
        user = get_object_or_404(CustomUser,id=id)
        user_serialized = UserSerializer(user)
        return JsonResponse(user_serialized.data, status=status.HTTP_200_OK)


