# Generated by Django 4.0 on 2022-02-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_profile', '0013_folder_folder_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_description',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
