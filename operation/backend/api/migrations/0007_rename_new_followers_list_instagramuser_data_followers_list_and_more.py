# Generated by Django 5.1.5 on 2025-02-20 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_new_list_instagramuser_data_new_followers_list_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instagramuser_data',
            old_name='new_followers_list',
            new_name='followers_list',
        ),
        migrations.RemoveField(
            model_name='instagramuser_data',
            name='old_followers_list',
        ),
    ]
