from django.db import models
from Hiring.models import Jobpost,Applicants 
from User.models import user 


class recommendation(models.Model):
    jobs = models.ForeignKey(Jobpost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user