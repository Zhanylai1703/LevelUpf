from django.db import models

from apps.courses.models import Course
from apps.tests.constants import LEVEL_CHOICES


class Adress(models.Model):
    region = models.CharField(
        max_length=255, verbose_name='Регион/Область'
    )
    adress = models.CharField(
        max_length=255, verbose_name='Адресс'
    )

    class Meta:
        verbose_name = 'Адресс'
        verbose_name_plural = 'Адресса'

    def __str__(self):
        return f'{self.region} - {self.adress}'


class FormForUser(models.Model):
    name = models.CharField(max_length=55, verbose_name="Имя Пользователя")
    surname = models.CharField(
        max_length=255, verbose_name="Фамилия Пользователя"
    )
    phone_number = models.CharField(
        max_length=20, verbose_name="Номер Пользователя"
    )
    email = models.EmailField(
        max_length=100, verbose_name="Email Пользователя"
    )
    adress = models.ForeignKey(
        Adress, verbose_name='Адресс',
        on_delete=models.CASCADE, related_name="FormForUsers"
    )

    class Meta:
        verbose_name = 'Форма для пользователя'
        verbose_name_plural = 'Форма для пользователей'

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name="Текст Вопроса")

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Test(models.Model):
    name = models.CharField(max_length=255, verbose_name='название теста')
    form_for_user = models.ForeignKey(
        FormForUser, verbose_name='Формы для пользователей',
        on_delete=models.CASCADE, related_name="tests"
    )
    course = models.ForeignKey(
        Course, verbose_name='Course',
        on_delete=models.CASCADE, related_name="tests"
    )
    question = models.ManyToManyField(Question, verbose_name='Вопросы')
    is_demo = models.BooleanField(default=False)
    level = models.CharField(
        max_length=10, choices=LEVEL_CHOICES
    )

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(
        Question, verbose_name='Вопрос',
        on_delete=models.CASCADE, related_name="answers"
    )
    is_true = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.question
