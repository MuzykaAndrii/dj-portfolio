from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='portfolios',
        verbose_name='User portfolio',
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Portfolio name',
    )
    avatar = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Image",
    )


class Skill(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='skills',
        verbose_name='Certain skill',
    )
