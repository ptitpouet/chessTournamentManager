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
        print(tournament.name + ' (' + tournament.date + ' : ' + tournament.location + ')' +
              str(tournament.nb_of_rounds) + ' rounds' + ' | ' +
              TIME_CONTROL[tournament.time_control])
        print(tournament.description)

    def display_round_details(self, starting_round):
        print("-------------------------------------------------------------------------------------------------------")
        print(str(starting_round.name))
        for match in starting_round.matches:
            print(str(match))
        print("-------------------------------------------------------------------------------------------------------")

    def display_all_match_results(self, round):
        print(round.name)
        for match in round.matches:
            print(match.result[0][0].firstname + " " + match.result[0][0].lastname
                  + " " + str(match.result[0][1]) + " | " + str(match.result[1][1]) + " " +
                  match.result[1][0].firstname + " " + match.result[1][0].lastname)
        print("-------------------------------------------------------------------------------------------------------")

    def display_tournament_overall_ranking(self, tournament):
        print("-------------------------------------------------------------------------------------------------------")
        print("TOURNAMENT OVERALL RANKING:")
        for attendee in tournament.attendees:
            print(attendee.firstname + " " + attendee.lastname + " : " + str(attendee.score))
        print("-------------------------------------------------------------------------------------------------------")

    def prompt_for_tournament_reset(self):
        userinput = input('     > Do you want to restart this Tournament? Y(es)[default] or N(o)')
        userinput = str(userinput).lower()
        if userinput == 'y' or userinput == 'yes' or userinput == 'oui' or userinput == 'o' or userinput == '':
            return True
        elif userinput == 'n' or userinput == 'no' or userinput == 'non':
            return False

    def prompt_for_match_result(self, match):
        print(str(match))
        print("     0 | " + "-- Draw Match --")
        print("     1 | " + match.white_player.firstname + ' ' + match.white_player.lastname)
        print("     2 | " + match.black_player.firstname + ' ' + match.black_player.lastname)

        try:
            return int(input("Select the winner ( 1 | 2 ) or Draw ( 0 ): "))
        except:
            print("!!! Error. Enter '1' or '2'")
            return -1

    def display_tournament_players(self, attendees):
        print("-------------------------------------------------------------------------------------------------------")
        print("Players List:")
        for attendee in attendees:
            print("|" + attendee.firstname + ' ' + attendee.lastname + ' (' \
                  + GENDER[attendee.gender] + '|' + attendee.birthday + ') - ' \
                  + "#" + str(attendee.rank))
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
