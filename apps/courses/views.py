from django.shortcuts import render

from rest_framework import generics

from apps.courses.serializers import CategorySerializer
from apps.courses.models import Category


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
