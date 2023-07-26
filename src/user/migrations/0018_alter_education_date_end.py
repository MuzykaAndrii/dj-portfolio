# Generated by Django 4.2.3 on 2023-07-26 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='date_end',
            field=models.DateField(blank=True, help_text='Enter date of education was ended, or leave blank if currently learning', null=True, verbose_name='Date of education ended'),
        ),
    ]