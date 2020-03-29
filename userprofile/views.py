from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response


class UserLoginApiView(ObtainAuthToken):
    """login view api class"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


"""ModelViewSet"""


"""ViewSet"""


"""API View"""




