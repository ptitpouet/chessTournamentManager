from tinydb import TinyDB

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
