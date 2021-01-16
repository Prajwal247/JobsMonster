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