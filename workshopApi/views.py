from django.shortcuts import render
from rest_framework import views
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def index(request):