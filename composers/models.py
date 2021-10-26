from django.db import models

# Create your models here.
class Composer(models.Model):
    name = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=200)
    born = models.CharField(max_length=50)
    died = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} by {self.period} ({self.id})"


