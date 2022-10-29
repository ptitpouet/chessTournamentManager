from .match import Match

class Round:
    def __init__(self, name, start, matches):
        self.name = name
        self.start = start
        self.end = 0
        self.matches = matches
