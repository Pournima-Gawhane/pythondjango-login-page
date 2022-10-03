from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render,HttpResponse
from rest_framework import generics
from .models import User_detail
from .serializers import UserSerializer
from .import models
from .import serializers



# Create your views here.
class ListUser_detail(generics.ListCreateAPIView):
    queryset =models.User_detail.objects.all()
    serializer_class = UserSerializer


class DetailUser_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User_detail.objects.all()
    serializer_class = UserSerializer
