from models.player import GENDER


class TournamentRunnerView:

    def show_welcome(self):
        """Welcome the user"""
        print('         ~~ Tournament START ~~         ')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

    def display_player(self, i, player):
        print(str(i) + "| " + player.firstname + ' ' + player.lastname
                            + ' (' + GENDER[player.gender] + '|' + player.birthday + ')')
