# Generated by Django 4.0.6 on 2022-08-01 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecards', '0005_followrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.DeleteModel(
            name='FollowRequest',
        ),
    ]