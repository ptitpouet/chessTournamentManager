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
        self.is_finished = False

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.location} ({self.date}). " \
               f"Rounds : {self.nb_of_rounds} | Mode : {TIME_CONTROL[self.time_control]}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def get_serialized_players_list(self, attendees):
        serialized_players = []
        if attendees is not None and len(attendees) > 0:
            for attendee in attendees:
                serialized_players.append(attendee.serialize())
        return serialized_players

    def get_serialized_rounds_list(self, rounds):
        serialized_rounds = []
        if rounds is not None and len(rounds) > 0:
            for round in rounds:
                serialized_rounds.append(round.serialize())
        return serialized_rounds

    def serialize(self):
        serialized_tournament = {
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'nb_of_rounds': self.nb_of_rounds,
            'description': self.description,
            'time_control': self.time_control,
            'attendees': self.get_serialized_players_list(self.attendees),
            'rounds': self.get_serialized_rounds_list(self.rounds),
            'is_finished': self.is_finished
        }
        return serialized_tournament
