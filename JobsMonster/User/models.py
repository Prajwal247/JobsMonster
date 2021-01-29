from __future__ import unicode_literals
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)


        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have superuser = True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have staff = True')

        else:
            return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    """
    model for user information
    """
    email = models.CharField(_('email'), max_length=50, unique=True)
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    is_active = models.BooleanField(_('active'), default=True, help_text='must be active if false the user is deleted')
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    avatar = models.ImageField(upload_to = 'avatars/', null = True, blank =True)

    occupations_choices = (
        ('Recruiter','RE'),
        ('Agriculture,Food and Natural Resources','AFNR'),
        ('Architecture and Construction','Architecture and Construction'),
        ('Technology and Communications','TECH'),
        ('Business Management and Administration','BMA'),
        ('Education and Training','EDU'),
        ('Finance','FIN'),
        ('Government and Public Administration','GOV'),
        ('Health Science','HS'),
        ('Hospitality and Tourism','HT'),
        ('Human Service','Humanservice'),
        ('Information Technology','IT'),
        ('Law and Pulblic Safety','LAW'),
        ('Manufacturing','MANU'),
        ('Sales and Marketing','Sales'),
        ('Engineering and Mathematics','Eng/Math'),
        ('Transportation','Trans'),
    )

    Specialization = models.CharField(max_length=100, choices=occupations_choices)
    Skills = models.TextField()
    work_experience = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    BioData = models.FileField(upload_to='biodata/')
    currently_employed = models.CharField(max_length=100)
    date_joined = models.DateField(_('date_joined'), default = timezone.now)
    DOB = models.CharField(max_length=20)
    Nationality = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ))

    pay_rate = models.FloatField(null = True, blank = True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def get_full_name(self):
        # returns full name of the user
        full_name = '%s %s'%(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def send_email(self,subject,message,from_email = None, **kwargs):
        # sends mail to this user
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email
