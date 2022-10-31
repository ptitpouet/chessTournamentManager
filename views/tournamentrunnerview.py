from models.player import GENDER


class TournamentRunnerView:

    def show_welcome(self):
        """Welcome the user"""
        print('         ~~ Tournament START ~~         ')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

    def display_player(self, i, player):
        print(str(i) + "| " + player.firstname + ' ' + player.lastname
              + ' (' + GENDER[player.gender] + '|' + player.birthday + ')')

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
            userinput = input('     > Add another player Y(es) or N(o)')
            userinput = str(userinput).lower()
            if userinput == 'y' or userinput == 'yes' or userinput == 'oui' or userinput == 'o':
                return True
            elif userinput == 'n' or userinput == 'no' or userinput == 'non':
                return False
        except:
            print("!!! Error. Enter 'Y' or 'N'). Operation aborted.")
