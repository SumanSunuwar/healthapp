from django.db import models

# Create your models here.
# model to represent patient for registering
class Patient(models.Model):
    name = models.CharField(max_length=255,unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name