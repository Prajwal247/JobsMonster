from django.db import models
import datetime
# Create your models here.
class HiringInfo(models.Model):
    Full_name = models.CharField(max_length=200, help_text='Your Full name')
    address = models.CharField(max_length=50, help_text = 'address must be valid and genuine')
    date = models.DateField(auto_now_add=False, help_text = 'Date for the reservation')
    Required_for = models.CharField(max_length = 100,help_text = 'Must be the area in which he/she is expert in')
    description = models.TextField(help_text = 'Full description of the work')
    estimated_duration = models.FloatField(help_text = 'For how many hour do you need him/her')
    contact_no = models.CharField(max_length = 14, help_text = 'Contact no of yours')

    def __str__(self):
        return self.Required_for


class Jobpost(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    category_choices = (
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
    category = models.CharField(max_length = 25, choices = category_choices)
    estimated_time = models.IntegerField(help_text = 'required time to complete the job in hr')


    def __str__(self):
        return self.title