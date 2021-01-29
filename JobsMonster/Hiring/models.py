from django.db import models
import datetime
from User.models import User

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
    date = models.DateField()
    category_choices = (
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
    category = models.CharField(max_length = 100, choices = category_choices)
    estimated_time = models.IntegerField(help_text = 'required time to complete the job in hr')
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title