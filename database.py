from tinydb import TinyDB

from models.player import Player
from models.tournament import Tournament

database_name = 'db.json'
players_table_name = 'players'
tournaments_table_name = 'tournaments'


class Database:

    def __init__(self):
        self.db = TinyDB(database_name)

    def save_list_in_database(self, table_name, list_to_save):
        database_table = self.db.table(table_name)  # get the table name
        database_table.truncate()  # delete the old table
        database_table.insert_multiple(list_to_save)

    def save_players_in_database(self, serialized_players_list):
        self.save_list_in_database(players_table_name, serialized_players_list)

    def save_tournament_in_database(self, serialized_tournaments_list):
        self.save_list_in_database(tournaments_table_name, serialized_tournaments_list)

    def get_serialized_objects_list(self, table_name):
        database_table = self.db.table(table_name)  # get the table name
        return database_table.all()

    def get_players_from_database(self):
        return self.get_serialized_objects_list(players_table_name)

    def get_tournaments_from_database(self):
        return self.get_serialized_objects_list(tournaments_table_name)

    def save_tournaments_list_in_database(self, tournaments_to_save):
        def get_serialized_tournament(tournaments_list_to_serialize):
            serialized_tournaments_list = []
            for tournament in tournaments_list_to_serialize:
                serialized_tournaments_list.append(tournament.serialize())

            return serialized_tournaments_list

        self.save_tournament_in_database(get_serialized_tournament(tournaments_to_save))

    def load_tournaments_list_from_database(self):
        tournaments_list = []
        serialized_tournaments_list_from_db = self.get_tournaments_from_database()

        if serialized_tournaments_list_from_db is not None:
            for serialized_tournament in serialized_tournaments_list_from_db:
                tournament = Tournament(serialized_tournament['name'],
                                        serialized_tournament['location'],
                                        serialized_tournament['date'],
                                        serialized_tournament['nb_of_rounds'],
                                        serialized_tournament['description'],
                                        serialized_tournament['time_control'])
                tournament.attendees = serialized_tournament['attendees']
                tournament.rounds = serialized_tournament['rounds']
                tournament.is_finished = serialized_tournament['is_finished']

                tournaments_list.append(tournament)

        return tournaments_list

    def update_tournament_in_database(self, tournament_updated):
        '''Load the tournaments in database, select the one and update'''
        tournaments_list = self.load_tournaments_list_from_database()
        i=0
        for tournament in tournaments_list:
            if tournament.name == tournament_updated.name \
                    and tournament.date == tournament_updated.date \
                    and tournament.location == tournament_updated.location:
                tournaments_list[i] = tournament_updated
                break
            i += 1
        self.save_tournaments_list_in_database(tournaments_list)

    def save_players_list_in_database(self, players_list_to_save):
        def get_serialized_players_list(players_list_to_serialize):
            serialized_players_list = []
            for player in players_list_to_serialize:
                serialized_players_list.append(player.serialize())

            return serialized_players_list

        self.save_players_in_database(get_serialized_players_list(players_list_to_save))

    def load_players_list_from_database(self):
        players_list = []
        serialized_players_list_from_db = self.get_players_from_database()

        if serialized_players_list_from_db is not None:
            for serialized_player in serialized_players_list_from_db:
                player = Player(serialized_player['lastname'],
                                serialized_player['firstname'],
                                serialized_player['birthday'],
                                serialized_player['gender'],
                                serialized_player['rank'])
                players_list.append(player)
        return players_list
