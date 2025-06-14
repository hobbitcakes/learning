from django.db import models
from django.contrib.auth.models import User

GAME_STATUS_CHOICES = (
    ('F', 'First Player to Move'),
    ('S', 'Second Player to Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw')
)

class Game(models.Model):
    first_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_first_player")
    second_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_second_player")
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

    def __str__(self):
        return "%s vs %s" % (self.first_player, self.second_player)
    

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game=models.ForeignKey(Game, on_delete=models.CASCADE)