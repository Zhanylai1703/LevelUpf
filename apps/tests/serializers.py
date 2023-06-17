from rest_framework import serializers

from apps.tests.models import (
    Question,
    Answer,
    Test,
    Course,
    FormForUser
)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'text',
        )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'id',
            'answer',

        )


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id',
            'name',
            'form_for_user',
            'course',
            'question',
            'is_demo',
            'level',
        )
