class Match:
    def __init__(self, white_player, black_player):
        self.white_player = white_player
        self.black_player = black_player
        self.result = ()

    def __str__(self):
        """Used in print."""
        return f"{self.white_player.firstname} {self.white_player.lastname}" \
               f" ({self.white_player.birthday}) - {self.white_player.score}" \
               f"  VS  " \
               f"{self.black_player.firstname} {self.black_player.lastname}" \
               f" ({self.black_player.birthday}) - {self.black_player.score}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def serialize(self):
        serialized_match = {
            'white_player': self.white_player,
            'black_player': self.black_player,
            'result': self.result,
        }
        return serialized_match

    def update_score(self, winner_player):
        """"""
        if winner_player == self.black_player:
            self.black_player.score += 1
            black_player_match_score = 1
            self.white_player.score += 0
            white_player_match_score = 0
        elif winner_player == self.white_player:
            self.white_player.score += 1
            white_player_match_score = 1
            self.black_player.score += 0
            black_player_match_score = 0
        elif winner_player is None:
            self.white_player.score += 0.5
            white_player_match_score = 0.5
            self.black_player.score += 0.5
            black_player_match_score = 0.5
        else:
            self.white_player.score += 0.5
            white_player_match_score = 0.5
            self.black_player.score += 0.5
            black_player_match_score = 0.5

        self.result = ([self.white_player, white_player_match_score], [self.black_player, black_player_match_score])
        return self.result
