import json
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import views, viewsets, mixins
from rest_framework.response import Response

from app import building_info, division_list
from app.models import Task
from app.serializers import TaskSerializer

User = get_user_model()

class BuildingInfoViewSet(mixins.ListModelMixin, 
                            viewsets.GenericViewSet):
    def list(self, request):
        return Response(building_info)

class DivisionViewSet(mixins.ListModelMixin, 
                            viewsets.GenericViewSet):
    def list(self, request):
        return Response(division_list)

class MechanicViewSet(mixins.ListModelMixin, 
                            viewsets.GenericViewSet):
    def list(self, request):
        return Response(Group.objects.get(name='mechanic')\
          .user_set.values('id', 'username', 'first_name', 'last_name')
        )

class TaskViewSet(mixins.CreateModelMixin, 
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
