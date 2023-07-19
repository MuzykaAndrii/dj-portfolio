from django.db import models

from user.models import Profile


class Language(models.Model):
    LEVELS = (
        ("A1", "(A1) Beginner"),
        ("A2", "(A2) Elementary"),
        ("B1", "(B1) Intermediate"),
        ("B2", "(B2) Upper Intermediate"),
        ("C1", "(C1) Advanced"),
        ("C2", "(C2) Proficient"),
        ("native", "Native")
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='languages',
        verbose_name='User that posses the languages',
    )
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="Name of the language",
    )
    level = models.CharField(
        max_length=10,
        choices=LEVELS,
        blank=False,
        null=False,
        verbose_name="Level of knowing the language",
    )

    def __str__(self):
        return f'{self.user} possess {self.name} with {self.level} level'