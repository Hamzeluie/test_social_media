from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .permissions import *

from .models import *
from .serializers import *


"""APIView"""


class PostApiView(APIView):
    pass


"""ViewSet"""


class PostViewSet(ViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnPosts,)
    serializer_class = PostModelSerializer
    model = Post

    def list(self, request, pk=None):
        obj = self.model.objects.all()
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=obj)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=obj, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'object id {pk} deleted'})


class CommentViewSet(ViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = CommentModelSerializer
    permission_classes = (UpdateOwnComments,)
    model = PostComment

    def list(self, request, pk=None):
        obj = self.model.objects.all()
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=obj)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=obj, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'object id {pk} deleted'})


"""ModelViewSet"""


class PostModelViewSet(ModelViewSet):
    pass


"""pure django"""
