# Generated by Django 4.0 on 2022-02-13 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_profile', '0011_remove_folder_folder_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='folder_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folderProfile', to='site_profile.profile'),
        ),
    ]
