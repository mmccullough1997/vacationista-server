from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=50)
  date_posted = models.DateField()
  content = models.CharField(max_length=255)
  image = models.CharField(max_length=255)
  thumbnail = models.CharField(max_length=255)
