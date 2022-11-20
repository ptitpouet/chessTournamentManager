from datetime import datetime

REPORT_OPTIONS = (
    'List of all players',
    'Tournament Report',
    '<- back'
)

TOURNAMENT_OPTIONS = (
    'List of players',
    'Tournament Results',
    '<- back'
)


class ReportMenuView:

    def show_welcome(self):
        """Welcome the user"""
        print('~~ Reports ~~')

    def prompt_for_section(self):
        """Prompt for the Main Menu"""
        user_choice = 0
        self.print_separator_line()
        print("     > What do you want to do?")

        def print_menu():
            for value in REPORT_OPTIONS:
                print(REPORT_OPTIONS.index(value) + 1, '--', value)

        print_menu()
        try:
            user_choice = int(input('     > Enter your choice: '))
        except ValueError:
            print('!!! Wrong input. Please enter a number between 1 and ' + str(len(REPORT_OPTIONS) + 1))

        return user_choice

    def prompt_for_sort_by_rank_or_alphabetic(self):
        """Ask the user if he want the list to be sorted by rank, otherwise by alphabetic order"""
        try:
            userinput = input('     > Do you want to sort the list by rank ? Y(es)[default] / N(o)[alphabetic order]')
            userinput = str(userinput).lower()
            if userinput == 'y' or userinput == 'yes' or userinput == 'oui' or userinput == 'o' or userinput == '':
                return True
            elif userinput == 'n' or userinput == 'no' or userinput == 'non':
                return False
            else:
                return False
        except ValueError:
            print('Wrong input. Please retry...')

    def display_player_with_position(self, i, player):
        print(str(i) + "| " + str(player))

    def display_player(self, player):
        print(str(player))

    def print_separator_line(self):
        print("------------------------------------------------------------------------------------------------------")

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
                raise ValueError(console_message)
        except ValueError:
            print('Wrong input. Please enter a valid number (between 1 and ' + str(length) + ')')
            self.prompt_for_tournament_id(length)

    def display_tournament_attendees(self, attendees):
        self.print_separator_line()
        print("TOURNAMENT ATTENDEES:")
        for attendee in attendees:
            print(attendee.lastname + " " + attendee.firstname + " : " + str(attendee.score))

    def display_round_details(self, current_round):
        self.print_separator_line()
        print(str(current_round.name))
        print("started on " + str(datetime.fromtimestamp(current_round.start).strftime("%m/%d/%Y at %H:%M")))
        for match in current_round.matches:
            print("<-- " + match.result[0][0].firstname + " " + match.result[0][0].lastname
                  + " " + str(match.result[0][1]) + " | " + str(match.result[1][1]) + " " +
                  match.result[1][0].firstname + " " + match.result[1][0].lastname + " -->")
        print("End of the round: " + str(datetime.fromtimestamp(current_round.end).strftime("%H:%M")))

    def prompt_for_list_interaction(self):
        """Prompt for the report list Options"""
        user_choice = 0
        self.print_separator_line()
        print("     > What do you want to do?")

        def print_menu():
            for value in TOURNAMENT_OPTIONS:
                print(TOURNAMENT_OPTIONS.index(value) + 1, '--', value)

        print_menu()
        try:
            user_choice = int(input('     > Enter your choice: '))
        except ValueError:
            print('!!! Wrong input. Please enter a number between 1 and ' + str(len(TOURNAMENT_OPTIONS) + 1))

        return user_choice

    def prompt_user_to_return(self):
        self.print_separator_line()
        user_input = input('     > Enter any key to return')
        return user_input
