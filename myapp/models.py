from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
ItemStatusChoices = [(0, 'PENDING'), (1,  'BOUGHT'), (0, 'NOT AVAILABLE')]


class GroceryList(models.Model):
    ItemName = models.CharField(max_length=50)
    ItemQuantity = models.IntegerField()
    ItemStatus = models.CharField(max_length=50, choices=ItemStatusChoices)
    Date = models.DateTimeField()

    class Meta:
        db_table = "list_of_grocery"


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


def __str__(self):
    return self.user.username
