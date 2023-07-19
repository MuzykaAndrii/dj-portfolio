from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('user', 'name'), name="Unique portfolio name constraint"),
        )


class Skill(models.Model):
    SKILL_TYPE = (
        ('hard', 'Hard skill'),
        ('soft', 'Soft skill'),
    )

    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='skills',
        verbose_name='Certain skill',
    )
    type = models.CharField(
        max_length=10,
        choices=SKILL_TYPE,
        verbose_name="Type of skill",
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Skill name',
    )
    level = models.PositiveSmallIntegerField(
        default=1,
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Level of possesing skill in grade from 1 to 10",
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Skill description",
    )

    def __str__(self):
        return f'{self.portfolio.user} {self.type} skill: {self.name} {self.level}/10'
    
    class Meta:
        verbose_name_plural = 'Skills'
        constraints = (
            models.UniqueConstraint(fields=('portfolio', 'name'), name='Unique skill name'),
        )
