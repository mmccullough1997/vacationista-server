from django.db import models

class ExpenseType(models.Model):
  label = models.TextField()
