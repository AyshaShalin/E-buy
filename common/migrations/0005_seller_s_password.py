# Generated by Django 4.1.1 on 2022-10-06 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_remove_customer_c_accholdername_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='s_password',
            field=models.CharField(default='', max_length=8),
        ),
    ]
