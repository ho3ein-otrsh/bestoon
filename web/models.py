from django.db import models
from django.contrib.auth.models import User

class Expense (models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "{}:{}".format(self.text,self.date)

class Income (models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "{}:{}".format(self.text,self.date)
