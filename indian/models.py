from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class GameSet(models.Model):
    player_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    player1money = 100000
    player1CardNumber = 0
    player2money = 100000
    player2CardNumber = 0
    bankerMoney = 0
    regame = False
    waitForRequest = "Please, wait Other Player"

    def __str__(self):
        return self.player_id
