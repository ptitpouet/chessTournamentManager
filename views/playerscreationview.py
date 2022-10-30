from models.player import GENDER


class PlayersCreationView:

    def show_welcome(self):
        """New User Creation"""
        print('~~ Player Creation ~~')

    def prompt_for_last_name(self):
        """Prompt for the player last name"""
        try:
            last_name = input('Enter the last name: ')
            return last_name
        except:
            print('Wrong input. Please retry...')

    def prompt_for_first_name(self):
        """Prompt for the player first name"""
        try:
            first_name = input('Enter the first name: ')
            return first_name
        except:
            print('Wrong input. Please retry...')

    def prompt_for_birthday(self):
        """Prompt for the player birthdate"""
        try:
            birthday = input('Enter the birthday (yyyy-mm-dd): ')
            return birthday
        except:
            print('Wrong input. Please retry...')

    def prompt_for_gender(self):
        """Prompt for the player gender"""
        user_choice = 0

        def print_menu():
            for value in GENDER:
                print(GENDER.index(value), '--', value)

        print_menu()
        try:
            user_choice = int(input('Enter your gender: '))
        except:
            print('Wrong input. Please enter a number ...')

        return user_choice

    def prompt_for_rank(self):
        """Prompt for the player rank"""
        try:
            rank = int(input("Enter the player's rank: "))
            return rank
        except:
            print('Wrong input. Please retry...')

    def prompt_for_another_player(self):
        """Prompt for additional player creation"""
        try:
            userinput = input('Do you want to create an additional player? Y(es) / N(o)')
            userinput = str(userinput).lower()
            if userinput == 'y' or userinput == 'yes' or userinput == 'oui' or userinput == 'o':
                return True
            elif userinput == 'n' or userinput == 'no' or userinput == 'non':
                return False
            else:
                return False
        except:
            print('Wrong input. Please retry...')
