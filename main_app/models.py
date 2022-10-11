from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Patient(models.Model):

    name = models.CharField(max_length=100)
    dob = models.DateField()
    diagnosis = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# class Record(models.Model):

#     reason = models.TextField()
#     vital_signs = models.TextField()
#     treatment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="records")


#     def __str__(self):
#         return self.reason
    