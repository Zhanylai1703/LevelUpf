# Generated by Django 4.2.2 on 2023-06-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subcategory",
            name="photo",
            field=models.FileField(default=1, upload_to="category/"),
            preserve_default=False,
        ),
    ]
