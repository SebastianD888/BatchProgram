from django.db import models

# Create your models here.
class Enter_Leave(models.Model):
    enter = models.CharField(max_length=100)
    leave = models.CharField(max_length=100)