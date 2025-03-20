from django.db import models

class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    time = models.FloatField()  # Time taken for 10 questions (lower is better) # Default to an empty list

    def __str__(self):
        return f"{self.name} - {self.time}s"

class Player(models.Model):
    name = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
<<<<<<< HEAD
    # score = models.IntegerField(default=0)
    # start_time = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.name} -  {'Complete' if self.is_complete else 'Incomplete'}"
    

class Winner(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

=======

    def __str__(self):
        return f"{self.name} -  {'Complete' if self.is_complete else 'Incomplete'}"
>>>>>>> b4c5730e8052513033a436a361ad9e1c103f2052
