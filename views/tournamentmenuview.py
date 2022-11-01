OPTIONS = (
    'Create a Tournament',
    'Tournament Manager',
    '< Exit >'
)


class TournamentMenuView:

    def show_welcome(self):
        """Welcome the user"""
        print('~~ Tournament Management ~~')

    def prompt_for_section(self):
        """Prompt for the Main Menu"""
        user_choice = 0
        print("------------------------------------------------")
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
