# Generated by Django 3.2.13 on 2022-05-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
    ]
