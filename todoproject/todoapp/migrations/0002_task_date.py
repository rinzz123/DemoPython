# Generated by Django 4.2.7 on 2023-12-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2020-10-14'),
            preserve_default=False,
        ),
    ]
