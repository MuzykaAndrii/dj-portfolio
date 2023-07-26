from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from user.models import Profile


class CV(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='cvs',
        verbose_name='User cv',
    )
    name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='CV name',
    )
    avatar = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Image",
    )
    info = models.TextField(
        blank=False,
        null=False,
        verbose_name='Personal information',
    )
    extra_info = models.TextField(
        blank=True,
        null=True,
        verbose_name="Extra information",
    )

    def __str__(self) -> str:
        return f'{self.profile} cv: {self.name}'

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('profile', 'name'), name="Unique cv name constraint"),
        )


class Skill(models.Model):
    SKILL_TYPE = (
        ('hard', 'Hard skill'),
        ('soft', 'Soft skill'),
    )

    cv = models.ForeignKey(
        CV,
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
        verbose_name="Level of possessing skill in grade from 1 to 10",
    )
    description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Skill description",
    )

    def __str__(self):
        return f'{self.cv.profile} {self.type} skill: {self.name} {self.level}/10'
    
    class Meta:
        verbose_name_plural = 'Skills'
        constraints = (
            models.UniqueConstraint(fields=('cv', 'name'), name='Unique skill name'),
        )
