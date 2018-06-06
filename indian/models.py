from django.db import models
from django.utils import timezone

# Create your models here.
class GameSet(models.Model):
    player1money = 100000
    player1CardNumber = 0
    player2money = 100000
    player2CardNumber = 0
    bankerMoney = 0
    regame = False
    waitForRequest = "Please, wait Other Player"
