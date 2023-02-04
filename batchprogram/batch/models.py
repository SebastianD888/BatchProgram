from django.db import models

# Create your models here.
class Enter_Leave(models.Model):
    enter = models.CharField(verbose_name="Enter-Time", max_length=100)
    leave = models.CharField(verbose_name="Leave-Time", max_length=100)
    def __str__(self):
        return f'from: {self.enter}, until: {self.leave}'