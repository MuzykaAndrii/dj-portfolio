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


