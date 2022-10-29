class HomeView:

    def show_welcome(self):
        """Welcome the user"""
        print('Welcome to the Chess Tournament Manager!')
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

    def prompt_for_section(self):
        """Prompt for the user's choice of what to do"""
        menu_options = {
            1: 'Manage the Players',
            2: 'Launch a new Tournament',
            3: 'Open the Report section',
            4: 'Exit',
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
        if option >= 1 or option <= 3:
            print_option(menu_options[option])
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

        return option



