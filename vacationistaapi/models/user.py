from django.db import models

class User(models.Model):
  uid = models.TextField()
  first_name = models.TextField()
  last_name = models.TextField()
  date_registered = models.DateField()
  username = models.TextField()
  bio = models.TextField()
  image = models.TextField()

  @property
  def events(self):
    return self.__events
  
  @events.setter
  def events(self, value):
    self.__events = value
