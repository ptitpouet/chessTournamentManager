class TournamentView:

    def show_welcome(self):
        """Welcome the user"""
        print('~~ Tournament Management ~~')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

    def prompt_for_section(self):
        """Prompt for the user's choice of what to do"""
        menu_options = {
            1: 'Launch a new Tournament',
            2: 'Load a Tournament',
            3: '- back'
        }

        def print_menu():
            for key in menu_options.keys():
                print(key, '--', menu_options[key])

        def print_option(option):
            print('--> '+ str(option))

        print("What do you want to do?")
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option >= 1 or option <= 2:
            print_option(menu_options[option])
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

        return option



