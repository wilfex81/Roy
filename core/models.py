from django.db import models


class Event(models.Model):
    host = models.CharField(max_length= 250)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length= 100)
    deadline = models.DateField()
    begining = models.DateField()
    image = models.ImageField(upload_to= 'Events')

    def __str__(self):
        return self.host

class Camp(models.Model):
    camp_name = models.CharField(max_length=150)
    about_camp = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Camp')

    def __str__(self):
        return self.camp_name