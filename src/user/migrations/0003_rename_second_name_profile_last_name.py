# Generated by Django 4.2.3 on 2023-07-19 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_name_profile_first_name_profile_birth_place_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='second_name',
            new_name='last_name',
        ),
    ]