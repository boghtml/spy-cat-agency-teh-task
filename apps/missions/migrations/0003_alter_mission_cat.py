# Generated by Django 5.0.6 on 2025-01-12 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
        ('missions', '0002_remove_mission_complete_mission_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cats.cat'),
        ),
    ]