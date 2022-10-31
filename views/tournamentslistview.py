OPTIONS = (
    'Launch a Tournament',
    'Add a new Tournament',
    'Delete a Tournament from database',
    'Reset all',
    '<- back'
)


class TournamentsListView:

    def print_separator_line(self):
        print("-------------------------------------------------------------------------------------------------------")

    def display_tournament(self, i, tournament):
        self.print_separator_line()
        print(str(i) + "| " + str(tournament))

    def prompt_for_tournament_id(self, length):
        """Prompt for Tournament id in list"""
        try:
            user_input = int(input("     > Enter the Tournament id in the list: "))
            if 0 < user_input <= length:
                return user_input
            else:
                console_message = 'your input shall be in the list range (1 to' + str(length) \
                                  + '). Value entered was: ' + str(user_input)
                print(console_message)
                raise Exception(console_message)
        except:
            print('Wrong input. Please enter a valid number (between 1 and ' + str(length) + ')')

    def prompt_for_tournament_deletion_confirmation(self, tournament):
        try:
            userinput = input('     > Confirm deletion of ' + tournament.name + '? Y(es) or N(o)')
            userinput = str(userinput).lower()
            if userinput == 'y' or userinput == 'yes' or userinput == 'oui' or userinput == 'o':
                return True
            elif userinput == 'n' or userinput == 'no' or userinput == 'non':
                return False
        except:
            print("!!! Error. Enter 'Y' or 'N'). Operation aborted.")

    def prompt_for_list_interaction(self):
        """Prompt for the players List Options"""
        user_choice = 0
        self.print_separator_line()
        print("     > What do you want to do?")

        def print_menu():
            for value in OPTIONS:
                print(OPTIONS.index(value) + 1, '--', value)

        print_menu()
        try:
            user_choice = int(input('     > Enter your choice: '))
        except:
            print('!!! Wrong input. Please enter a number between 1 and ' + str(len(OPTIONS) + 1))

        return user_choice