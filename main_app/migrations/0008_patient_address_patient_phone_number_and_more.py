# Generated by Django 4.1.1 on 2022-10-12 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.TextField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default=12, max_length=10),
        ),
        migrations.AlterField(
            model_name='provider',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='providers', to='main_app.patient'),
        ),
    ]
