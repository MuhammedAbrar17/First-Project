# Generated by Django 4.2.3 on 2023-09-09 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0010_admincategory_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admincategory',
            name='offer',
        ),
    ]
