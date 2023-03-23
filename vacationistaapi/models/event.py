from django.db import models
from .event_type import EventType
from .trip import Trip
from .leg import Leg

class Event(models.Model):
  event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
  leg = models.ForeignKey(Leg, on_delete=models.CASCADE, blank=True, null=True)
  description = models.TextField()
  location = models.TextField()
  date = models.DateField(blank=True, null=True)
  image = models.TextField(blank=True, null=True)
  title = models.TextField()

  @property
  def user(self):
    return self.__user
  
  @user.setter
  def user(self, value):
    self.__user = value
