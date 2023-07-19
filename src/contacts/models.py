from django.db import models
from user.models import Profile


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
    