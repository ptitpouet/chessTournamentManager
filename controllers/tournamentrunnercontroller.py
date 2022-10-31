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
            #self.db.update_tournament_in_database



    def display_players_list(self, players_list):
        '''Return a list, in case we sort the list'''
        i = 0
        for player in players_list:
            i += 1
            self.view.display_player(i, player)
        return players_list

    def add_players_in_attendees_list(self, players_list):
        if players_list is None or len(players_list) == 0:
            players_list = self.db.load_players_list_from_database()

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
    def generate_match_pairs_with_swiss_system(self, players_list, isFirstTour):
        def sort_players_by_score_then_rank(players_list):
            return sorted(players_list, key=attrgetter('score', 'rank', 'birthday'), reverse=True)

        def generate_first_tour_matches_pairs(sorted_list):
            matches = []
            for i in range(0, int(len(sorted_list) / 2), 1):
                matches.append(Match(sorted_list[i], sorted_list[i + int(len(sorted_list) / 2)]))
            return matches

        def generate_following_tour_matches_pairs(sorted_list):
            matches = []
            while len(sorted_list) >= 2:
                print("in the while")
                for j in range(1, len(sorted_list), 1):
                    print(j)
                    print(sorted_list[j].opponent_list.name)
                    if sorted_list[0] not in sorted_list[j].opponent_list:
                        matches.append(Match(sorted_list[0], sorted_list[j]))
                        sorted_list.pop(j)
                        sorted_list.pop(0)
                        break
                    else:
                        print("else")
            return matches

        sorted_list = sort_players_by_score_then_rank(players_list)
        if isFirstTour:
            return generate_first_tour_matches_pairs(sorted_list)
        else:
            return generate_following_tour_matches_pairs(sorted_list)
