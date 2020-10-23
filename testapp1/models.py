from django.db import models

# Create your models here.
class todo(models.Model):
    text = models.CharField(max_length= 50, blank=False)
    description = models.CharField(max_length=35, blank=True)
