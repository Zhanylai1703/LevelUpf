# Generated by Django 4.2.2 on 2023-06-18 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tests", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="testresult",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tests",
                to="courses.course",
                verbose_name="Course",
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="form_for_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tests",
                to="tests.formforuser",
                verbose_name="Формы для пользователей",
            ),
        ),
        migrations.AddField(
            model_name="test",
            name="question",
            field=models.ManyToManyField(to="tests.question", verbose_name="Вопросы"),
        ),
        migrations.AddField(
            model_name="test",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tests",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="offlineregistration",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tests.adress",
                verbose_name="Адрес",
            ),
        ),
        migrations.AddField(
            model_name="offlineregistration",
            name="test",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="tests.test",
                verbose_name="Событие",
            ),
        ),
        migrations.AddField(
            model_name="offlineregistration",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="formforuser",
            name="adress",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="FormForUsers",
                to="tests.adress",
                verbose_name="Адресс",
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="tests.question",
                verbose_name="Вопрос",
            ),
        ),
    ]
