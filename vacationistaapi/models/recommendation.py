from django.db import models

class Recommendation(models.Model):
  title = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  description = models.CharField(max_length=255, null=True, blank=True)
  location = models.CharField(max_length=255)
  rating = models.DecimalField(max_digits=20, decimal_places=2)
  image = models.CharField(max_length=255, null=True, blank=True)
