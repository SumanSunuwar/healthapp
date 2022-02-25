from django.db import models

from register.models import Patient

# Create your models here.
# model to represent patient for registering
class Order(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.patient