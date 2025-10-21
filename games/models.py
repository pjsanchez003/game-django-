from django.db import models
from django.urls import reverse

PLATFORMS = [("PC","PC"), ("PS5","PlayStation 5"), ("XBOX","Xbox"), ("SWITCH","Nintendo Switch")]

class Game(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=20, choices=PLATFORMS)
    genre = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    cover = models.ImageField(upload_to="covers/", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("games:game-detail", args=[self.pk])

# Create your models here.
