# Generated by Django 5.0.2 on 2024-03-02 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lesson'),
        ),
    ]
