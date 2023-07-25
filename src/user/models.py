from django.db import models
from django.contrib.auth.models import User

from django.db.models import Q


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User profile",
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="User name",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="User last name",
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
        verbose_name="Date of birth",
    )
    birth_place = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Place of birth",
    )
    residence_place = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Current live place",
    )

    def save(self, *args, **kwargs):
        if not self.residence_place:
            self.residence_place = self.birth_place

        super(Profile, self).save(*args, **kwargs)

    @property
    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.surname}'
    
    def __str__(self) -> str:
        return f'user: {self.user}, {self.full_name}'
    
    class Meta:
        verbose_name_plural = 'Profiles'


class Contact(models.Model):
    CONTACT_TYPES = (
        ('phone', 'Phone number'),
        ('email', 'Email address'),
        ('telegram', 'Telegram'),
        ('viber', 'Viber'),
        ('github', 'Github'),
        ('linkedin', 'Linkedin'),
    )
    profile = models.ForeignKey(
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
    data = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name="Contact data (link, nickname, etc.)",
    )

    def __str__(self) -> str:
        return f'{self.type} contact of {self.profile}, data: {self.data}'
    
    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('profile', 'type', 'data'), name='Contact uniqueness'),
        )
        verbose_name_plural = 'Contacts'


class Education(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='education_set',
    )
    institution = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Education institution name',
    )
    degree = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Degree or level of education',
    )
    speciality = models.CharField(
        max_length=255,
        verbose_name='Speciality of learning',
    )
    date_start = models.DateField(
        null=False,
        blank=False,
        verbose_name='Date of education beginning',
    )
    date_end = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of education ended',
        help_text='Enter date of education was ended, or leve blank if currently learning',
    )

    def __str__(self) -> str:
        return f'Education of {self.profile} in {self.institution}'
    
    class Meta:
        verbose_name_plural='Education',
        constraints = (
            models.UniqueConstraint(fields=(
                'profile',
                'institution',
                'degree',
                'speciality'
            ),
            name='Education unique constraint'),
        )
        ordering = [
            '-date_end',
        ]
        

class Employment(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='employments',
    )
    company_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Company name',
    )
    position = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Position',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Job description',
    )
    date_start = models.DateField(
        null=False,
        blank=False,
        verbose_name='Start date',
    )
    date_end = models.DateField(
        null=True,
        blank=True,
        verbose_name='End date',
        help_text='Leave blank if currently employed',
    )

    def __str__(self) -> str:
        return f'Employment of {self.profile} in {self.company_name}'
    
    class Meta:
        verbose_name_plural='Employments',


class Course(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Course name',
    )
    certificate = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        null=False,
        blank=False,
        verbose_name='Course certificate',
    )

    def __str__(self):
        return f'Course: {self.name} user: {self.profile}'
    
    class Meta:
        verbose_name_plural = 'Courses'


class Project(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='projects',
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Project name',
    )
    link = models.URLField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Link to hosted project',
    )
    source = models.URLField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Link to project repository',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Description of project",
    )

    def __str__(self):
        return f'{self.name} project of {self.profile}'
    
    class Meta:
        verbose_name_plural = 'Projects'
        constraints = [
            models.UniqueConstraint(fields=('profile', 'name'), name='Project uniqueness'),
            models.CheckConstraint(
                check=~Q(Q(link__isnull=True) | Q(link__iexact='')) | ~Q(Q(source__isnull=True) | Q(source__iexact='')),
                name='Either link or source code should be specified',
            ),
        ]