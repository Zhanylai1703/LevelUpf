from rest_framework import serializers

from apps.courses.models import Category, Course, Faq
from apps.tests.models import FormForUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent',
            'photo',
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'title',
            'subtitle',
            'category',
            'description',
            'photo',
        )


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = (
            'question',
            'answer',
        )


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormForUser
        fields = (
            'name',
            'phone_number',
            'feedback',
        )
