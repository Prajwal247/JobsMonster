from django.db import models

# Create your models here.

class Occupation(models.Model):

    occupations_choices = (
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
    Skills = models.TextField(max_length = 200)