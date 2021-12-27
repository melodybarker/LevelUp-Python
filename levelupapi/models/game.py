from django.db import models

from .gametype import GameType
from .gamer import Gamer

class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='game_creator')
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE, related_name='game_type')
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()