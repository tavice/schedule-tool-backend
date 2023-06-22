from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Activity, Resource, TeamMember, ProjectManager
from .serializers import ProjectSerializer, ActivitySerializer, ResourceSerializer, TeamMemberSerializer, ProjectManagerSerializer
from rest_framework.response import Response

# Project viewset
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print('instance is', instance)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# Activity viewset
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# Resource viewset
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# TeamMember viewset
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

# ProjectManager viewset
class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer
