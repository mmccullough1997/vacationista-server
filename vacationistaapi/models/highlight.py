from django.db import models

class Highlight(models.Model):
  title = models.CharField(max_length=50)
  content = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  thumbnail = models.CharField(max_length=255)
