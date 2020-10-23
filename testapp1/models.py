from django.db import models

# Create your models here.
class todo(models.Model):
    text = models.Charfield(max_length= 50, blank=False)
    