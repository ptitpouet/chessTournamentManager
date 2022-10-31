from models.match import Match
from models.player import Player
from views.homeview import HomeView
from operator import attrgetter
from random import randint
from datetime import datetime


class TournamentRunnerController:

    def __init__(self, view, tournament, database):
        # views
        self.view = view
        self.db = database
        self.tournament = tournament

    def run(self):
        self.view.show_welcome()
        self.initial_check_tournament(self.tournament)
        print(self.tournament.attendees)

    def back_home(self):
        self.view = HomeView()
        self.run()

    def initial_check_tournament(self, tournament):
        if tournament.attendees is None or len(tournament.attendees) == 0:
            self.add_players_in_attendees_list(None)

    def display_players_list(self, players_list):
        '''Return a list, in case we sort the list'''
        i = 0
        for player in players_list:
            i += 1
            self.view.display_player(i, player)
        return players_list

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
                players_list.append(player)
        return players_list

    def add_players_in_attendees_list(self, players_list):
        if players_list is None or len(players_list) == 0:
            players_list = self.load_players_list_from_database()

        players_list = self.display_players_list(players_list)
        players_list = self.add_attendees_in_list(players_list)

        if self.view.prompt_for_add_another_player():
            self.add_players_in_attendees_list(players_list)

    def add_attendees_in_list(self, all_players_list):
        index_player_id = self.select_player(all_players_list)
        player = all_players_list[index_player_id]
        self.tournament.attendees.append(player)
        all_players_list.pop(index_player_id)
        return all_players_list

    def select_player(self, all_players_list):
        if len(all_players_list) > 0:
            player_id = self.view.prompt_for_player_id(len(all_players_list))
            if player_id is not None:
                index_player_id = player_id - 1
                return index_player_id
            else:
                self.select_player(all_players_list)

    # méthode de tri des joueurs
    def generate_match_pairs_with_swiss_system(self, playersList, isFirstTour):
        def sort_players_by_score_then_rank(playersList):
            return sorted(playersList, key=attrgetter('score', 'rank', 'birthday'), reverse=True)

        def generate_first_tour_matches_pairs(sortedList):
            matches = []
            for i in range(0, int(len(sortedList) / 2), 1):
                matches.append(Match(sortedList[i], sortedList[i + int(len(sortedList) / 2)]))
            return matches

        def generate_following_tour_matches_pairs(sortedList):
            matches = []
            while len(sortedList) >= 2:
                print("in the while")
                for j in range(1, len(sortedList), 1):
                    print(j)
                    print(sortedList[j].opponent_list.name)
                    if sortedList[0] not in sortedList[j].opponent_list:
                        matches.append(Match(sortedList[0], sortedList[j]))
                        sortedList.pop(j)
                        sortedList.pop(0)
                        break
                    else:
                        print("else")
            return matches

        sorted_list = sort_players_by_score_then_rank(playersList)
        if isFirstTour:
            return generate_first_tour_matches_pairs(sorted_list)
        else:
            return generate_following_tour_matches_pairs(sorted_list)
