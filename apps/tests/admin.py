from django.contrib import admin
from apps.tests.models import Answer, Question, Test


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass
