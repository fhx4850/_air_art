# Generated by Django 4.0 on 2022-02-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_profile', '0008_alter_profile_profile_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follow',
            new_name='FollowModel',
        ),
    ]
