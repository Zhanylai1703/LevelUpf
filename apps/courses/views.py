from django.shortcuts import render

from rest_framework import generics, filters
from apps.courses.managers import FeedbackMessageManager

from apps.courses.serializers import(
    CategorySerializer,
    CourseSerializer,
    FaqSerializer,
    FeedbackSerializer
)
from apps.courses.models import Category, Course, Faq
from apps.tests.models import FormForUser


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
    queryset = Faq.objects.all()


class FeedbackMessageCreateView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        feedback_message = serializer.save()
        return FeedbackMessageManager.perform_create(feedback_message)
