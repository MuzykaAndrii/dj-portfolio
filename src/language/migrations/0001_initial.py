# Generated by Django 4.2.3 on 2023-07-19 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_rename_name_profile_first_name_profile_birth_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name of the language')),
                ('level', models.CharField(choices=[('A1', '(A1) Beginner'), ('A2', '(A2) Elementary'), ('B1', '(B1) Intermediate'), ('B2', '(B2) Upper Intermediate'), ('C1', '(C1) Advanced'), ('C2', '(C2) Proficient'), ('Native', 'Native')], max_length=10, verbose_name='Level of knowing the language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='user.profile', verbose_name='User that posses the languages')),
            ],
        ),
    ]