from django.shortcuts import render
from rest_framework import viewsets
from .models import Project, Activity, Resource, TeamMember, ProjectManager
from .serializers import ProjectSerializer, ActivitySerializer, ResourceSerializer, TeamMemberSerializer, ProjectManagerSerializer

# Create your views here.
#Project viewset
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


#Activity viewset
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


#Resource viewset
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


#TeamMember viewset
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


#ProjectManager viewset
class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer
    
        