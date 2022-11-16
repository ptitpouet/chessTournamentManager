class PlayerMenuController:
    def __init__(self, view, controller, database):
        # views
        self.view = view
        self.controller = controller
        self.db = database

    def run(self):
        self.view.show_welcome()
        self.display_menu_options()

    def display_menu_options(self):
        option = self.view.prompt_for_section()

        if option == 1:
            self.create_player()
        elif option == 2:
            players_list = self.display_players_list()
            self.display_players_list_options(players_list)
        elif option == 3:
            self.back_home()
        else:
            self.display_menu_options()

    def back_home(self):
        self.controller.home_controller.run()

    def display_players_list(self):
        players_list = self.db.load_players_list_from_database()
        i = 0
        for player in players_list:
            i += 1
            self.view.display_player(i, player)
        return players_list

    def display_players_list_options(self, players_list):
        if len(players_list) > 0:
            option = self.view.prompt_for_list_interaction()
            if option == 1:
                self.create_player()
            elif option == 2:
                self.update_rank()
            elif option == 3:
                self.delete_player()
            elif option == 4:
                self.reset_players_database()
        else:
            self.view.display_warning_database_empty()
        self.display_menu_options()

    def reset_players_database(self):
        self.db.reset_players_table()

    def delete_player(self):
        players_list = self.display_players_list()
        player_id = self.view.prompt_for_player_id(len(players_list))
        if player_id is not None:
            index_player_id = player_id - 1

            if self.view.prompt_for_player_deletion_confirmation(players_list[index_player_id]):
                players_list.pop(index_player_id)

            print("This is a simulated call to action")
            self.db.save_players_list_in_database(players_list)

            self.display_players_list_options(players_list)
        else:
            self.display_players_list_options(players_list)

    def update_rank(self):
        players_list = self.display_players_list()
        player_id = self.view.prompt_for_player_id(len(players_list))
        if player_id is not None:
            player_id = player_id - 1

            new_rank = self.view.prompt_for_player_rank_update(players_list[player_id])
            players_list[player_id].rank = new_rank

            self.db.save_players_list_in_database(players_list)
            self.display_players_list_options(players_list)
        else:
            self.display_players_list_options(players_list)

    def create_player(self):
        self.controller.player_creation_controller.run()
