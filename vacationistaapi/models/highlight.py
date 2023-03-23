from django.db import models

class Highlight(models.Model):
  title = models.TextField()
  content = models.TextField()
  image = models.TextField()
  location = models.TextField()
  thumbnail = models.TextField()
