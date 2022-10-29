class Match:
    def __init__(self, whitePlayer, blackPlayer):
        self.whitePlayer = whitePlayer
        self.whitePlayer.opponent_list.append(blackPlayer)
        self.blackPlayer = blackPlayer
        self.blackPlayer.opponent_list.append(whitePlayer)
        self.result = ()

    def updateScore(self, winnerPlayer):

        if winnerPlayer == self.blackPlayer:
            self.blackPlayer.score += 1
            blackPlayerMatchScore = 1
            self.whitePlayer.score += 0
            whitePlayerMatchScore = 0
        elif winnerPlayer == self.whitePlayer:
            self.whitePlayer.score += 1
            whitePlayerMatchScore = 1
            self.blackPlayer.score += 0
            blackPlayerMatchScore = 0
        elif winnerPlayer is None:
            self.whitePlayer.score += 0.5
            whitePlayerMatchScore = 0.5
            self.blackPlayer.score += 0.5
            blackPlayerMatchScore = 0.5
        else:
            self.whitePlayer.score += 0.5
            whitePlayerMatchScore = 0.5
            self.blackPlayer.score += 0.5
            blackPlayerMatchScore = 0.5

        self.result = ([self.whitePlayer, whitePlayerMatchScore], [self.blackPlayer, blackPlayerMatchScore])
        return self.result



