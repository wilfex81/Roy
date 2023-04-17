from django.db import models


class Event(models.Model):
    title = models.CharField(max_length= 250)
    description = models.CharField(max_length=100)
    area = models.CharField(max_length= 100)
    image = models.ImageField(upload_to= 'Events')

    def _str_(self):
        return self.title

class Camp(models.Model):
    camp_name = models.CharField(max_length=150)
    about_camp = models.CharField(max_length=300)
    image = models.ImageField(upload_to='Camp')

    def _str_(self):
        return self.camp_name

class ContactsSaved(models.Model):
    subject = models.CharField(max_length= 200)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.subject