from django.db import models
from django.contrib.auth.models import User

class Expense (models.Model):
    text=models.CharField(max_length=255)
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
