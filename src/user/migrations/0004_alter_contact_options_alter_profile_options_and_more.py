# Generated by Django 4.2.3 on 2023-07-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_second_name_profile_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='User last name'),
        ),
        migrations.AddConstraint(
            model_name='contact',
            constraint=models.UniqueConstraint(fields=('user', 'type', 'link'), name='Contact uniqueness'),
        ),
    ]