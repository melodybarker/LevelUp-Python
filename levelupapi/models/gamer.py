from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class Gamer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField('levelupapi.Event', related_name='attendees')
    bio = models.TextField(max_length=500)