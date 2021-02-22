from django.db import models
import datetime
from User.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="duration of the projects")
    estimated_manpowers = models.IntegerField(help_text="total number of people estimated to complete the project")
    initiated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ProjectManpowers(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"project+{self.project_id}"

class Update(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title