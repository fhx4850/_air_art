# Generated by Django 4.0 on 2022-02-08 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_profile', '0006_remove_profile_profile_id_profileid_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileid',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_id', to='site_profile.profile'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='site_profile.profile')),
                ('Follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='site_profile.profile')),
            ],
        ),
    ]
