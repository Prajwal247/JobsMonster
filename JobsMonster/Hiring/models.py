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
        ('Recruiter','Recruiter'),
        ('Agriculture,Food and Natural Resources','Agriculture,Food and Natural Resources'),
        ('Architecture and Construction','Architecture and Construction'),
        ('Technology and Communications','Technology and Communications'),
        ('Business Management and Administration','Business Management and Administration'),
        ('Education and Training','Education and Training'),
        ('Finance','Finance'),
        ('Government and Public Administration','Government and Public Administration'),
        ('Health Science','Health Science'),
        ('Hospitality and Tourism','Hospitality and Tourism'),
        ('Human Service','Humanservice'),
        ('Information Technology','Information Technology'),
        ('Law and Pulblic Safety','Law and Pulblic Safety'),
        ('Manufacturing','Manufacturing'),
        ('Sales and Marketing','Sales and Marketing'),
        ('Engineering and Mathematics','Engineering and Mathematics'),
        ('Transportation','Transportation'),
    )
    category = models.CharField(max_length = 100, choices = category_choices)
    estimated_time = models.IntegerField(help_text = 'required time to complete the job in hr')
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class Applicants(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    jobpost_id = models.ForeignKey(Jobpost, on_delete=models.CASCADE)
    applied_date = models.DateField()

    def __str__(self):
        return f"applicants+{self.jobpost_id}"

