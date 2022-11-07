from .match import Match

class Round:
    def __init__(self, name, start, matches):
        self.name = name
        self.start = start
        self.end = None
        self.matches = []

    def close_round(self, end, matches):
        self.end = end
        self.matches = matches

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.start}"



