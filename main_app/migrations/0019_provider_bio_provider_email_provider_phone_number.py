# Generated by Django 4.1.1 on 2022-10-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_alter_provider_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='bio',
            field=models.TextField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='provider',
            name='email',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='provider',
            name='phone_number',
            field=models.CharField(default=0, max_length=12),
        ),
    ]
