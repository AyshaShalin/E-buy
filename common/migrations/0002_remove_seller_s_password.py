# Generated by Django 4.1.1 on 2022-10-05 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='s_password',
        ),
    ]
