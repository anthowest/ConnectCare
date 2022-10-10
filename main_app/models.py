from django.db import models

# Create your models here.
class Provider(models.Model):

    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Patient(models.Model):

    name = models.CharField(max_length=100)
    dob = models.DateField()
    diagnosis = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']