from models.tournament import TIME_CONTROL


class TournamentCreationView:

    def show_welcome(self):
        """New Tournament"""
        print('~~ New Tournament ~~')

    def prompt_for_tournament_name(self):
        """Prompt for the tournament's name"""
        try:
            name = input('Enter a name for the Tournament: ')
            return name
        except:
            print('Wrong input. Please retry...')

    def prompt_for_tournament_location(self):
        """Prompt for the tournament location"""
        try:
            location_name = input('Enter the location: ')
            return location_name
        except:
            print('Wrong input. Please retry...')

    def prompt_for_tournament_date(self):
        """Prompt for the tournament date"""
        try:
            date = input('Enter the date (yyyy-mm-dd): ')
            return date
        except:
            print('Wrong input. Please retry...')

    def prompt_for_tournament_nb_of_rounds(self):
        """Prompt for the player rank"""
        try:
            nbofrounds = int(input("Number of rounds: "))
            return nbofrounds
        except:
            print('Wrong input. Please retry...')

    def prompt_for_tournament_description(self):
        """Prompt for the tournament description"""
        try:
            description = input('Enter the description: ')
            return description
        except:
            print('Wrong input. Please retry...')

    def prompt_for_tournament_time_control(self):
        """Prompt for the tournament time control"""
        user_choice = 0
        def print_menu():
            for value in TIME_CONTROL:
                print(TIME_CONTROL.index(value), '--', value)
        print_menu()
        try:
            user_choice = int(input('Enter what Time Control: '))
        except:
            print('Wrong input. Please enter a number ...')
        return user_choice

