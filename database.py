from tinydb import TinyDB

from models.match import Match
from models.player import Player
from models.round import Round
from models.tournament import Tournament

database_name = 'db.json'
players_table_name = 'players'
tournaments_table_name = 'tournaments'


class Database:

    def __init__(self):
        self.db = TinyDB(database_name)

    def add_object_in_database(self, table_name, object):
        database_table = self.db.table(table_name)  # get the table name
        database_table.insert(object)

    def replace_list_in_database(self, table_name, list_to_save):
        database_table = self.db.table(table_name)  # get the table name
        database_table.truncate()  # delete the old table
        database_table.insert_multiple(list_to_save)

    def get_serialized_objects_list(self, table_name):
        database_table = self.db.table(table_name)  # get the table name
        return database_table.all()

    def reset_table_database(self, table_name):
        database_table = self.db.table(table_name)
        database_table.truncate()

    def insert_tournament_in_database(self, tournament):
        self.add_object_in_database(tournaments_table_name, tournament.serialize())

    def save_tournaments_list_in_database(self, tournaments_to_save):
        def get_serialized_tournament(tournaments_list_to_serialize):
            serialized_tournaments_list = []
            for tournament in tournaments_list_to_serialize:
                serialized_tournaments_list.append(tournament.serialize())

            return serialized_tournaments_list

        self.replace_list_in_database(tournaments_table_name, get_serialized_tournament(tournaments_to_save))

    def load_tournaments_list_from_database(self):
        tournaments_list = []
        serialized_tournaments_list_from_db = self.get_serialized_objects_list(tournaments_table_name)

        if serialized_tournaments_list_from_db is not None:
            for serialized_tournament in serialized_tournaments_list_from_db:
                tournament = self.deserialize_tournament(serialized_tournament)
                tournaments_list.append(tournament)

        return tournaments_list

    def deserialize_tournament(self, serialized_tournament):
        tournament = Tournament(serialized_tournament['name'],
                                serialized_tournament['location'],
                                serialized_tournament['date'],
                                serialized_tournament['nb_of_rounds'],
                                serialized_tournament['description'],
                                serialized_tournament['time_control'])
        for serialized_player in serialized_tournament['attendees']:
            tournament.attendees.append(self.deserialize_player(serialized_player))
        for serialized_round in serialized_tournament['rounds']:
            tournament.rounds.append(self.deserialize_round(serialized_round))
        tournament.is_finished = serialized_tournament['is_finished']
        return tournament

    def update_tournament_in_database(self, tournament_updated):
        '''Load the tournaments in database, select the one and update'''
        tournaments_list = self.load_tournaments_list_from_database()
        i = 0
        for tournament in tournaments_list:
            if tournament.name == tournament_updated.name \
                    and tournament.date == tournament_updated.date \
                    and tournament.location == tournament_updated.location:
                tournaments_list[i] = tournament_updated
                break
            i += 1
        self.save_tournaments_list_in_database(tournaments_list)

    def reset_tournaments_table(self):
        self.reset_table_database(tournaments_table_name)

    def insert_player_in_database(self, player):
        self.add_object_in_database(players_table_name, player.serialize())

    def save_players_list_in_database(self, players_list_to_save):
        def get_serialized_players_list(players_list_to_serialize):
            serialized_players_list = []
            for player in players_list_to_serialize:
                serialized_players_list.append(player.serialize())

            return serialized_players_list

        self.replace_list_in_database(players_table_name, get_serialized_players_list(players_list_to_save))

    def load_players_list_from_database(self):
        players_list = []
        serialized_players_list_from_db = self.get_serialized_objects_list(players_table_name)

        if serialized_players_list_from_db is not None:
            for serialized_player in serialized_players_list_from_db:
                player = self.deserialize_player(serialized_player)
                players_list.append(player)
        return players_list

    def reset_players_table(self):
        self.reset_table_database(players_table_name)

    def deserialize_player(self, serialized_player):
        player = Player(serialized_player['lastname'],
                        serialized_player['firstname'],
                        serialized_player['birthday'],
                        serialized_player['gender'],
                        serialized_player['rank'])

        player.score = serialized_player['score']
        return player

    def deserialize_round(self, serialized_round):
        round = Round(serialized_round['name'],
                      serialized_round['start'],
                      serialized_round['end'],
                      serialized_round['is_finished'])
        for serialized_match in serialized_round['matches']:
            round.matches.append(self.deserialize_match(serialized_match))
        return round

    def deserialize_match(self, serialized_match):
        match = Match(self.deserialize_player(serialized_match['white_player']),
                      self.deserialize_player(serialized_match['black_player']),
                      serialized_match['is_finished'])
        if match.is_finished:
            match.result = ([match.white_player, serialized_match['white_player_match_score']],
                            [match.black_player, serialized_match['black_player_match_score']])
        return match
