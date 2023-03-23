from django.db import models

class Article(models.Model):
  title = models.TextField()
  date_posted = models.DateField()
  content = models.TextField()
  image = models.TextField()
  thumbnail = models.TextField()
