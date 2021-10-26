from django.db import models

# Create your models here.
class Piece(models.Model):
    title = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name