# Generated by Django 5.0 on 2025-03-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
