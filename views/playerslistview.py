class PlayersListView:

    def display_player(self, i, player):
        print("________________________________________________")
        print(str(i) + "| " + str(player))

    def prompt_for_player_id(self):
        """Prompt for player id in list"""
        try:
            i = int(input("Enter the player's id in the list: "))
            return i
        except:
            print('Wrong input. Please retry...')
            self.prompt_for_player_id()

    def confirm_deletion(self, player):
        userinput = input('Do you confirm deletion of '+ player.firstname + " " + player.lastname +'? Y(es)')
        if userinput == 'Y' or userinput == 'yes':
            return True
        else:
            return False

    def update_player_rank(self, player):
        """Prompt for update player rank"""
        try:
            rank = int(input("New rank value for "+ player.firstname + " " + player.lastname + " :"))
            return rank
        except:
            print('Wrong input. Please retry...')
            self.update_player_rank(player)

    def prompt_for_list_interaction(self):
        """Prompt for the user's choice of what to do"""
        menu_options = {
            1: 'Delete Player',
            2: 'Update Rank',
            3: '<- back'
        }

        def print_menu():
            for key in menu_options.keys():
                print(key, '    --', menu_options[key])

        def print_option(option):
            print('--> ' + str(option))

        print("________________________________________________")
        print("    What do you want to do?")
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option >= 1 or option <= 3:
            print_option(menu_options[option])
        else:
            print('Invalid option. Please enter a number between 1 and 3.')

        return option
