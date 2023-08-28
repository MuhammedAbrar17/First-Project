# Generated by Django 4.2.3 on 2023-08-26 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_remove_userprofile_referral_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='referral_code',
            field=models.CharField(default='hg', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='referred_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profile.userprofile'),
        ),
    ]