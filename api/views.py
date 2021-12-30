from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class StudentAPI(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    authentication_classes=[BasicAuthentication]