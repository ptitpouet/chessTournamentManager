from .match import Match

class Round:
    def __init__(self, name, start, matches):
        self.name = name
        self.start = start
        self.end = None
        self.matches = matches
        self.is_finished = False

    def close_round(self, end, matches):
        self.end = end
        self.matches = matches
        self.is_finished = True

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.start}"



