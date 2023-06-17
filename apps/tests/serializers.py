from rest_framework import serializers

from apps.tests.models import (
    Question,
    Answer,
    Test,
    Course,
    FormForUser
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
