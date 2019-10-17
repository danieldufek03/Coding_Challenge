from django.shortcuts import render
from .models import User, Organization, UserOrganization
from rest_framework import viewsets
from .serializers import UserSerializer, OrganizationSerializer, UserOrganizationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer



class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field = "name"
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class UserOrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field = "name"
    queryset = UserOrganization.objects.all()
    serializer_class = UserOrganizationSerializer
