from .match import Match


class Round:
    def __init__(self, name, start, end, is_finished):
        self.name = name
        self.start = start
        self.end = end
        self.is_finished = is_finished
        self.matches = []

    def start_round(self, start_time, matches):
        self.start = start_time
        self.matches = matches

    def close_round(self, end_time):
        self.end = end_time
        self.is_finished = True

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.start}"

    def get_serialized_matches_list(self, matches):
        serialized_matches = []
        if matches is not None and len(matches) > 0:
            for match in matches:
                serialized_matches.append(match.serialize())
        return serialized_matches

    def serialize(self):
        serialized_round = {
            'name': self.name,
            'start': self.start,
            'end': self.end,
            'is_finished': self.is_finished,
            'matches':  self.get_serialized_matches_list(self.matches)
        }
        return serialized_round
