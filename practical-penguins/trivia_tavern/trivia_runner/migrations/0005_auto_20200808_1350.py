# Generated by Django 3.0.8 on 2020-08-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_runner', '0004_auto_20200808_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activetriviaquiz',
            name='session_code',
            field=models.CharField(default='TYE3SY', editable=False, max_length=6, unique=True),
        ),
    ]
