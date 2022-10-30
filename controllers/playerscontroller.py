from views.homeview import HomeView
from views.playerscreationview import PlayersCreationView
from views.playerslistview import PlayersListView
from views.playersmenuview import PlayersMenuView
from models.player import Player


class PlayersController:
    def __init__(self, view, database):
        # views
        self.view = view
        self.db = database

    def run(self):

        self.view.show_welcome()

        option = self.view.prompt_for_section()

        if option == 1:
            self.create_player()
            self.display_menu()
        elif option == 2:
            self.display_players_list()
        elif option == 3:
            self.back_home()
        else:
            pass

    def back_home(self):
        self.view = HomeView()
        self.run()

    def display_menu(self):
        self.view = PlayersMenuView()
        self.run()

    def display_players_list(self):
        self.view = PlayersListView()

        players_list = self.load_players_list_from_database()
        i = 0
        for player in players_list:
            i += 1
            self.view.display_player(i, player)

        if len(players_list) > 0:
            option = self.view.prompt_for_list_interaction()
            if option == 1:
                self.create_player()
                self.display_menu()
            elif option == 2:
                self.update_rank(players_list)
            elif option == 3:
                self.delete_player(players_list)
            elif option == 4:
                self.reset_players_database()
            elif option == 5:
                self.display_menu()
            else:
                self.display_menu()
        else:
            self.display_menu()

    def reset_players_database(self):
        pass

    def delete_player(self, players_list):
        player_id = self.view.prompt_for_player_id(len(players_list))
        if player_id is not None:
            index_player_id = player_id - 1

            if self.view.prompt_for_player_deletion_confirmation(players_list[index_player_id]):
                players_list.pop(index_player_id)

            self.save_players_list_in_database(players_list)
            self.display_players_list()
        else:
            self.delete_player(players_list)

    def update_rank(self, players_list):
        player_id = self.view.prompt_for_player_id(len(players_list))
        if player_id is not None:
            player_id = player_id - 1

            new_rank = self.view.prompt_for_player_rank_update(players_list[player_id])
            players_list[player_id].rank = new_rank

            self.save_players_list_in_database(players_list)
            self.display_players_list()
        else:
            self.update_rank(players_list)

    def create_player(self):
        players_list = self.load_players_list_from_database()

        self.view = PlayersCreationView()
        self.view.show_welcome()

        def get_last_name():
            last_name = self.view.prompt_for_last_name()
            if last_name is None:
                get_last_name()
            else:
                return last_name

        def get_first_name():
            first_name = self.view.prompt_for_first_name()
            if first_name is None:
                get_first_name()
            else:
                return first_name

        def get_birthday():
            birthday = self.view.prompt_for_birthday()
            if birthday is None:
                get_birthday()
            else:
                return birthday

        def get_gender():
            gender = self.view.prompt_for_gender()
            if gender is None:
                get_gender()
            else:
                return gender

        def get_rank():
            rank = self.view.prompt_for_rank()
            if rank is None:
                get_rank()
            else:
                return rank

        players_list.append(Player(get_last_name(), get_first_name(), get_birthday(), get_gender(), get_rank()))
        self.save_players_list_in_database(players_list)

        if self.view.prompt_for_another_player():
            self.create_player()

    def save_players_list_in_database(self, players_list_to_save):
        def get_serialized_players_list(players_list_to_serialize):
            serialized_players_list = []
            for player in players_list_to_serialize:
                serialized_players_list.append(player.serialize())

            return serialized_players_list

        self.db.save_players_in_database(get_serialized_players_list(players_list_to_save))

    def load_players_list_from_database(self):
        players_list = []
        serialized_players_list_from_db = self.db.get_players_from_database()

        if serialized_players_list_from_db is not None:
            for serialized_player in serialized_players_list_from_db:
                player = Player(serialized_player['lastname'],
                                serialized_player['firstname'],
                                serialized_player['birthday'],
                                serialized_player['gender'],
                                serialized_player['rank'])
                player.score = serialized_player['score']
                player.opponent_list = serialized_player['opponent_list']
                players_list.append(player)
        return players_list
