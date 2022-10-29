from typing import List
from .player import Player
from .round import Round

TIME_CONTROL = ("bullet", "blitz", "fast")

class Tournament:
    def __init__(self, name, location, date, nbofRounds,
                 description, timeControl):
        self.name = name
        self.location = location
        self.date = date
        self.nbofRounds = nbofRounds
        self.description = description
        self.timeControl = TIME_CONTROL.index(timeControl)
        self.attendees = []
        self.rounds = []
