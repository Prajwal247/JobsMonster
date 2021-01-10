from django.db import models
from django.core.mail import send_mail
import random 
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone 
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from occupations.models import Occupation

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True 

    def _create_user(self, email, password, **extra_fields):
        """
        creates user and saves them with given username, email and password
        """
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user 

    def create_user(self, email = None, password = None , **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
 

class User(AbstractBaseUser, PermissionsMixin):
    """
    model for user informations extended
    """
    first_name = models.CharField(_('first name'), max_length=200, blank=True)
    last_name = models.CharField(_('last name'), max_length=200, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=20, unique=True, blank=True, null=True)
    avatar = models.ImageField(upload_to = 'static/img')
    is_staff = models.BooleanField(
        _('staff status'),
        default= False,
        help_text= 'allocates whether the user is staff or not'
    )
    is_active = models.BooleanField(
        _('active'),
        default = True,
        help_text = 'Allocates whether is active or not unselect this in case of deleting acounts'
    )
    
    occupations_choices = (
        ('RE','Recruiter'),
        ('AFNR','Agriculture,Food and Natural Resources'),
        ('A/C','Architecture and Construction'),
        ('Technology','Arts, Technology and Communications'),
        ('BMA','Business Management and Administration'),
        ('EDU','Education and Training'),
        ('FIN','Finance'),
        ('GOV','Government and Public Administration'),
        ('HS','Health Science'),
        ('HT','Hospitality and Tourism'),
        ('Humanservice','Human Service'),
        ('IT','Information Technology'),
        ('LAW','Law and Pulblic Safety'),
        ('Manufacture','Manufacturing'),
        ('sales','Sales and Marketing'),
        ('Eng/math','Engineering and Mathematics'),
        ('Trans','Transportation'),
    )

    Specialization = models.CharField(max_length = 20, choices = occupations_choices)
    Skills = models.TextField(max_length = 200, null = True, blank = True)

    location = models.CharField(max_length = 200, null = True)
    BioData = models.FileField(upload_to='static/biodata')
    work_experience = models.CharField(max_length=250, help_text = 'Previous Workexperience blank if not worked yet')
    currently_employed = models.CharField(max_length=50, help_text = 'Currently employed if any')
    pay_rate = models.FloatField(help_text = 'Expected pay rate per hour')
    date_joined = models.DateTimeField(_('date joined'), default = timezone.now)
    Gender = models.CharField(max_length=10, default = '', blank = True, null = True, help_text='gender of the user')
    DOB = models.CharField(max_length=20, null=True, blank=True, help_text='Date of birth of the user')
    Nationality = models.CharField(max_length=25, null=True, blank=True, help_text='Nationality of the user')

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_fullname(self):
        """return the full name of the user"""
        return f'{self.first_name} {self.last_name}'

    def get_shortname(self):
        """return the short name i.e firstname of the user"""
        return self.first_name

    def email_user(self, subject, message, from_email = None, **kwargs):
        """Sends the email with the message subject to the User"""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email