from typing import List
from .player import Player
from .round import Round

TIME_CONTROL = ("bullet", "blitz", "fast")

class Tournament:
    def __init__(self, name, location, date, nb_of_rounds,
                 description, time_control):
        self.name = name
        self.location = location
        self.date = date
        self.nb_of_rounds = nb_of_rounds
        self.description = description
        self.time_control = time_control
        self.attendees = []
        self.rounds = []


    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.location} ({self.description}" \
               f" - {self.date}). Rounds : {self.nb_of_rounds} | Mode : {TIME_CONTROL[self.time_control]}"

    def __repr__(self):
        """Used in print."""
        return str(self)