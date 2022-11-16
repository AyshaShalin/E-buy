# Generated by Django 4.1.1 on 2022-11-07 08:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_rename_c_name_customer_c_secondname_and_more'),
        ('seller', '0001_initial'),
        ('customer', '0003_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.BigIntegerField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
    ]
