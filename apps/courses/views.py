from django.shortcuts import render

from rest_framework import generics, filters

from apps.courses.serializers import CategorySerializer, CourseSerializer, FaqSerializer
from apps.courses.models import Category, Course, Faq


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class FAQListView(generics.ListAPIView):
    serializer_class = FaqSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']
    queryset = Faq.objects.all()
