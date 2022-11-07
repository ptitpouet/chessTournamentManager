from models.player import GENDER
from models.tournament import TIME_CONTROL


class TournamentRunnerView:

    @staticmethod
    def show_welcome():
        """Welcome the user"""
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print('                                         ~~ Tournament LAUNCH ~~                                       ')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

    def display_tournament_details(self, tournament):
        print(tournament.name + ' (' + tournament.date + ' : ' + tournament.location + ')')
        print(tournament.description)
        print(str(tournament.nb_of_rounds) + ' rounds' + ' | ' + TIME_CONTROL[tournament.time_control])

    def display_tournament_players(self, attendees):
        print("-------------------------------------------------------------------------------------------------------")
        for attendee in attendees:
            print("|" + attendee.lastname + ' ' + attendee.firstname + ' (' \
                    + GENDER[attendee.gender] + '|' + attendee.birthday + ') - ' \
                    + str(attendee.rank))
        print("-------------------------------------------------------------------------------------------------------")

    def display_player_to_pick(self, i, player):
        print(str(i) + "| " + player.firstname + ' ' + player.lastname
              + ' (' + GENDER[player.gender] + '|' + player.birthday + ')')

    def display_warning_no_players(self):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Players database empty. You need to add players first")

    def prompt_for_player_id(self, length):
        """Prompt for Player id in list"""
        try:
            user_input = int(input("     > Enter the Player id to add to the Tournament: "))
            if 0 < user_input <= length:
                return user_input
            else:
                console_message = 'your input shall be in the list range (1 to' + str(length) \
                                  + '). Value entered was: ' + str(user_input)
                print(console_message)
                raise Exception(console_message)
        except:
            print('Wrong input. Please enter a valid number (between 1 and ' + str(length) + ')')

    def prompt_for_add_another_player(self):
        try:
            userinput = input('     > Add another player Y(es)[default] or N(o)')
            userinput = str(userinput).lower()
            if userinput == 'y' or userinput == 'yes' or userinput == 'oui' or userinput == 'o' or userinput == '':
                return True
            elif userinput == 'n' or userinput == 'no' or userinput == 'non':
                return False
        except:
            print("!!! Error. Enter 'Y' or 'N'). Operation aborted.")
