# Generated by Django 4.1 on 2023-01-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_documentpred"),
    ]

    operations = [
        migrations.AddField(
            model_name="documentpred",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
