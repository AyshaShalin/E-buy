# Generated by Django 4.1.1 on 2022-10-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_seller_s_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='s_pic',
            field=models.ImageField(default='', upload_to='seller/'),
        ),
    ]
