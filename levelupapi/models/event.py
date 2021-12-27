from django.db import models

from .game import Game
from .gamer import Gamer
from .status import Status

class Event(models.Model):

    host = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='event_creator')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='events')
    location = models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    time = models.TimeField(max_length=50)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='game_status')
