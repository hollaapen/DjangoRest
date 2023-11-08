from django.shortcuts import render

from .models import Products, Students

from .serializers import ProductSerializer, StudentSerializer
from rest_framework import viewsets


class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


