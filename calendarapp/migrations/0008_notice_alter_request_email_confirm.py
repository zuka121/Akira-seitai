# Generated by Django 5.0.6 on 2024-10-09 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0007_request_email_confirm_alter_request_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='request',
            name='email_confirm',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス(確認)'),
        ),
    ]
