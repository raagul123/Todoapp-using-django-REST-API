from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from django.db.models import OuterRef,Subquery
from django.db.models import Q
from todo import serializers
from todo import models
from todo import permissions





class UserTodoViewSet(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.UserTodoSerializer
    qs = models.UserProfile.objects.all()
    queryset=models.TodoItem.objects.all()
    permissions_classes=(
        permissions.UpdateOwnTodo,
        IsAuthenticated
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'todo')


    def perform_create(self,serializer):
        serializer.save(profile_id=self.request.user)
    def get_queryset(self):
        return models.TodoItem.objects.filter(profile_id=self.request.user)


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permissions_classes=(permissions.UpdateOwnProfile,)
    def get_queryset(self):
        return models.UserProfile.objects.filter(username=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
    