# Generated by Django 5.0.6 on 2025-01-12 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
        ('missions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='complete',
        ),
        migrations.AddField(
            model_name='mission',
            name='status',
            field=models.CharField(choices=[('assigned', 'Assigned'), ('complete', 'Complete')], default='assigned', max_length=20),
        ),
        migrations.AlterField(
            model_name='mission',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cats.cat'),
            preserve_default=False,
        ),
    ]
