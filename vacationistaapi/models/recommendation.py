from django.db import models

class Recommendation(models.Model):
  title = models.TextField()
  category = models.TextField()
  description = models.TextField(null=True, blank=True)
  location = models.TextField()
  rating = models.DecimalField(max_digits=20, decimal_places=2)
  image = models.TextField(null=True, blank=True)
