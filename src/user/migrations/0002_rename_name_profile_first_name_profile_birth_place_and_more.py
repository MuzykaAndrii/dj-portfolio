# Generated by Django 4.2.3 on 2023-07-19 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_place',
            field=models.CharField(default='defaultname', max_length=200, verbose_name='Place of birth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='residence_place',
            field=models.CharField(default='defaultresidence', max_length=200, verbose_name='Current live place'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('phone', 'Phone number'), ('email', 'Email address'), ('telegram', 'Telegram'), ('viber', 'Viber'), ('linkedin', 'Linkedin')], max_length=30, verbose_name='Contact type')),
                ('link', models.CharField(max_length=200, verbose_name='Link to contact')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='user.profile', verbose_name='Contact owner')),
            ],
        ),
    ]
