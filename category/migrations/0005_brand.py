# Generated by Django 4.2.1 on 2023-07-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, unique=True)),
                ('brand_desc', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
