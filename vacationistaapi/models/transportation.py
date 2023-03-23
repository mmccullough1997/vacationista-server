from django.db import models
from .transportation_type import TransportationType
from .trip import Trip
from .leg import Leg

class Transportation(models.Model):
  transportation_type = models.ForeignKey(TransportationType, on_delete=models.CASCADE)
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
  leg = models.ForeignKey(Leg, on_delete=models.CASCADE, null=True, blank=True)
  travel_from = models.TextField()
  travel_to = models.TextField()
  amount = models.DecimalField(max_digits=20, decimal_places=2)
  comment = models.TextField()
  round_trip = models.BooleanField()
