from django.db import models
from django.utils import timezone

# Create your models here.
class GameSet(models.Model):
    player1money = models.PositiveIntegerField(default=100000)
    player1CardNumber = models.PositiveIntegerField()
    player2money = models.PositiveIntegerField(default=100000)
    player2CardNumber = models.PositiveIntegerField()
    bankerMoney = models.PositiveIntegerField(default=0)
    regame = models.BooleanField(default=True)
