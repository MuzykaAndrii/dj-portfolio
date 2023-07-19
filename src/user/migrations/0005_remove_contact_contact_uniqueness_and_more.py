# Generated by Django 4.2.3 on 2023-07-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_contact_options_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='contact',
            name='Contact uniqueness',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='user',
            new_name='profile',
        ),
        migrations.AddConstraint(
            model_name='contact',
            constraint=models.UniqueConstraint(fields=('profile', 'type', 'link'), name='Contact uniqueness'),
        ),
    ]