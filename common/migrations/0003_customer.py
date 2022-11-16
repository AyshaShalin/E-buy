# Generated by Django 4.1.1 on 2022-10-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_seller_s_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=20)),
                ('c_email', models.CharField(max_length=70)),
                ('c_phone', models.BigIntegerField()),
                ('c_Address', models.CharField(max_length=300)),
                ('c_accnumber', models.BigIntegerField()),
                ('c_ifsc', models.CharField(max_length=70)),
                ('c_accholdername', models.CharField(max_length=20)),
                ('c_password', models.CharField(max_length=8)),
            ],
        ),
    ]
