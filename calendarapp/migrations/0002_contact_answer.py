# Generated by Django 5.0.6 on 2024-12-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]