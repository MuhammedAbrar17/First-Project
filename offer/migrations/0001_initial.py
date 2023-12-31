# Generated by Django 4.2.1 on 2023-08-23 05:21

from django.db import migrations, models
import offer.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=10)),
                ('min_amount', models.PositiveBigIntegerField()),
                ('off_percent', models.PositiveIntegerField()),
                ('max_discount', models.PositiveIntegerField()),
                
            ],
        ),
    ]
