GENDER = ("none", "male", "female")


class Player:
    def __init__(self, lastname, firstname, birthday, gender, rank):
        self.lastname = lastname
        self.firstname = firstname
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.score = 0
        self.opponent_list = []

    def __str__(self):
        """Used in print."""
        return f"{self.firstname} {self.lastname} ({GENDER[self.gender]} - {self.birthday}). Rank : {self.rank}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def serialize(self):
        serialized_player = {
            'lastname': self.lastname,
            'firstname': self.firstname,
            'birthday': self.birthday,
            'gender': self.gender,
            'rank': self.rank,
        }
        return serialized_player
