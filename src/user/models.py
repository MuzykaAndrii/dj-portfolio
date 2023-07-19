from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User profile",
    )
    name = models.CharField(
        max_length=50,
        verbose_name="User name",
    )
    second_name = models.CharField(
        max_length=50,
        verbose_name="User second name",
    )
    surname = models.CharField(
        max_length=50,
        verbose_name="User surname",
        blank=True,
        null=True,
    )
    date_birth = models.DateField(
        blank=False,
        null=False,
        verbose_name="Date of user birth",
    )
    birth_place = models.CharField(
        max_length=200,
        verbose_name="Place of birth",
    )
    residence_place = models.CharField(
        max_length=200,
        verbose_name="Current live place",
    )


class Contact(models.Model):
    CONTACT_TYPES = (
        ('phone', 'Phone number'),
        ('email', 'Email address'),
        ('telegram', 'Telegram'),
        ('viber', 'Viber'),
        ('linkedin', 'Linkedin'),
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='contacts',
        verbose_name="Contact owner",
    )
    type = models.CharField(
        max_length=30,
        choices=CONTACT_TYPES,
        blank=False,
        null=False,
        verbose_name="Contact type"
    )
    link = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name="Link to contact",
    )


