from views.playerscreationview import PlayersCreationView
from views.playerslistview import PlayersListView
from views.playersmenuview import PlayersMenuView
from models.player import Player


class PlayersController:
    players_list = []

    def __init__(self, view):
        # views
        self.view = view

    def run(self):
        self.view.show_welcome()

        option = self.view.prompt_for_section()

        if option == 1:
            self.create_player()
            self.display_menu()
        elif option == 2:
            self.display_players_list(self.players_list)
        elif option == 3:
            pass
        else:
            pass

    def display_menu(self):
        self.view = PlayersMenuView()
        self.run()

    def display_players_list(self, players_list):
        self.view = PlayersListView()
        i = 0
        for player in players_list:
            i += 1
            self.view.display_player(i, player)
        if len(players_list) > 0:
            option = self.view.prompt_for_list_interaction()
            if option == 1:
                self.delete_player()
            elif option == 2:
                self.update_rank()
            elif option == 3:
                self.display_menu()
            else:
                self.display_menu()
        else:
            self.display_menu()

    def delete_player(self):
        player_id = self.view.prompt_for_player_id()

        if (self.view.confirm_deletion(self.players_list[player_id - 1])):
            self.players_list.pop(player_id - 1)

        self.display_players_list(self.players_list)

    def update_rank(self):
        player_id = self.view.prompt_for_player_id()
        new_rank = self.view.update_player_rank(self.players_list[player_id - 1])
        self.players_list[player_id - 1].rank = new_rank

        self.display_players_list(self.players_list)

    def create_player(self):
        self.view = PlayersCreationView()
        self.view.show_welcome()
        last_name = self.view.prompt_for_last_name()
        first_name = self.view.prompt_for_first_name()
        birthday = self.view.prompt_for_birthday()
        gender = self.view.prompt_for_gender()
        rank = self.view.prompt_for_rank()

        self.players_list.append(Player(last_name, first_name, birthday, gender, rank))

        if self.view.prompt_for_another_player():
            self.create_player()

    def serialized_players_list(self):
        serialized_players_list = []
        for player in self.players_list:
            serialized_player = player.serialize()
            serialized_players_list.append(serialized_player)

        return serialized_players_list
