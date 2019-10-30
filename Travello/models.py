from django.db import models


gender_opt = (
    ('male','MALE'),
    ('female', 'FEMALE'),
)
# Create your models here.
class Acceptors(models,Model):
    Firstname = models.CharField(max_length=75)
    Lastname = models.CharField(max_length=75)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    Gender = models.CharField(max_length=6, choices=gender_opt, default='')
    Bloodgroup = models.CharField(max_length= 10)
    Issuedate = models.DateField(auto_now=False, auto_now_add=False)
    Address = models.CharField(max_lenght=75)
    Contactnumber = models.CharField(max_length=12)

    def __str__(self):
        return self.Firstname






