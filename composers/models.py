from django.db import models
from piece.models import Piece

# Create your models here.
class Composer(models.Model):
    name = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    cover_image = models.CharField(max_length=200)
    born = models.CharField(max_length=50)
    died = models.CharField(max_length=50),
    piece = models.ForeignKey(
        Piece,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='composers'
    )

    def __str__(self):
        return f"{self.name} by {self.period} ({self.id})"


