# Generated by Django 4.2.2 on 2023-06-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_adress_formforuser_adress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adress',
            options={'verbose_name': 'Адресс', 'verbose_name_plural': 'Адресса'},
        ),
        migrations.AddField(
            model_name='formforuser',
            name='feedback',
            field=models.TextField(default=1, verbose_name='Обратная связь'),
            preserve_default=False,
        ),
    ]
