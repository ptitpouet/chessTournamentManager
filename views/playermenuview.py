MENU_OPTIONS = (
    'Create a new Player',
    'Players Database',
    '<- back'
)

PLAYER_OPTIONS = (
    'Add a new Player',
    'Update a Player Rank',
    'Delete a Player from database',
    'Reset database',
    '<- back'
)


class PlayerMenuView:

    def show_welcome(self):
        """Welcome the user"""
        print('~~ Players Administration ~~')

    def display_warning_database_empty(self):
        self.print_separator_line()
        print('!!! Player Database empty. Please add players')

    def prompt_for_section(self):
        """Prompt for the players Administration"""
        user_choice = 0
        self.print_separator_line()
        print("     > What do you want to do?")

        def print_menu():
            for value in MENU_OPTIONS:
                print(MENU_OPTIONS.index(value) + 1, '--', value)

        print_menu()
        try:
            user_choice = int(input('Enter your choice: '))
        except ValueError:
            print('!!! Wrong input. Please enter a number between 1 and ' + str(len(MENU_OPTIONS) + 1))

        return user_choice

    def print_separator_line(self):
        print("------------------------------------------------------------------------------------------------------")

    def display_player(self, i, player):
        self.print_separator_line()
        print(str(i) + "| " + str(player))

    def prompt_for_player_id(self, length):
        """Prompt for player id in list"""
        try:
            user_input = int(input("     > Enter the player's id in the list: "))
            if 0 < user_input <= length:
                return user_input
            else:
                console_message = 'your input shall be in the list range (1 to' + str(length) \
                                  + '). Value entered was: ' + str(user_input)
                print(console_message)
                raise Exception(console_message)
        except ValueError:
            print('Wrong input. Please enter a valid number (between 1 and ' + str(length) + ')')

    def prompt_for_player_deletion_confirmation(self, player):
        try:
            userinput = input('     > Please confirm deletion of ' + player.firstname + " " + player.lastname +
                              '? Y(es) or N(o)')
            userinput = str(userinput).lower()
            if userinput == 'y' or userinput == 'yes' or userinput == 'oui' or userinput == 'o' or userinput == '':
                return True
            elif userinput == 'n' or userinput == 'no' or userinput == 'non' or userinput == '':
                return False
        except ValueError:
            print("!!! Error. Enter 'Y' or 'N'). Operation aborted.")

    def prompt_for_player_rank_update(self, player):
        """Prompt for update player rank"""
        try:
            rank = int(input("     > New rank value for " + player.firstname + " " + player.lastname + " :"))
            if rank > 0:
                print('Success. Rank updated')
                return rank
            else:
                console_message = 'Input shall be a positive integer value. (> ' + rank + ')'
                print(console_message)
                raise Exception(console_message)
        except ValueError:
            print('!!! Error wrong value. Operation aborted')

    def prompt_for_list_interaction(self):
        """Prompt for the players List Options"""
        user_choice = 0
        self.print_separator_line()
        print("     > What do you want to do?")

        def print_menu():
            for value in PLAYER_OPTIONS:
                print(PLAYER_OPTIONS.index(value) + 1, '--', value)

        print_menu()
        try:
            user_choice = int(input('Enter your choice: '))
        except ValueError:
            print('!!! Wrong input. Please enter a number between 1 and ' + str(len(PLAYER_OPTIONS) + 1))

        return user_choice
