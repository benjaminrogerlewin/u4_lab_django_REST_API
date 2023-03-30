from django.db import models

# Create your models here.

class Team(models.Model):
    name =models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    devision = models.CharField(max_length=100)
    number_of_wins = models.IntegerField()
    number_of_losses = models.IntegerField()

    def __str__(self):
        return self.name
    
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    on_injured_reserved = models.BooleanField()

    def __str__(self):
        return self.name