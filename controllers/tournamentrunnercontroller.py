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
        self.initial_check_for_attendees(self.tournament)
        self.view.display_tournament_details(self.tournament)
        self.view.display_tournament_players(self.sort_players_by_alphabet_order(self.tournament.attendees))

        matches = (self.create_matches_of_round(self.tournament, True))

        for match in matches:
            print(str(match))

        # print(self.create_matches_of_round(self.tournament, False))

    def back_home(self):
        self.view = HomeView()
        self.run()

    def sort_players_by_alphabet_order(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=attrgetter('lastname', 'firstname', 'birthday'), reverse=True)

    def sort_players_by_score_then_rank(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=attrgetter('score', 'rank', 'birthday'), reverse=True)

    def create_matches_of_round(self, tournament, is_first_tour):

        def generate_first_tour_matches_pairs(sorted_list):
            """On the 1st round, the list is split in 2 half. 1st player of the first half play with first of 2nd"""
            matches = []
            for i in range(0, int(len(sorted_list) / 2), 1):
                matches.append(Match(sorted_list[i], sorted_list[i + int(len(sorted_list) / 2)]))
            return matches

        def generate_following_tour_matches_pairs(sorted_list):
            """On the 2nd and following rounds, players play against each other, based on their current score"""
            matches = []
            while len(sorted_list) >= 2:
                # print("in the while")
                for j in range(1, len(sorted_list), 1):
                    # print(j)
                    # print(sorted_list[j].opponent_list)
                    if sorted_list[0] not in sorted_list[j].opponent_list:
                        matches.append(Match(sorted_list[0], sorted_list[j]))
                        sorted_list.pop(j)
                        sorted_list.pop(0)
                        break
            return matches

        sorted_list = self.sort_players_by_score_then_rank(tournament.attendees)
        if is_first_tour:
            return generate_first_tour_matches_pairs(sorted_list)
        else:
            return generate_following_tour_matches_pairs(sorted_list)

    def initial_check_for_attendees(self, tournament):
        if tournament.attendees is None or len(tournament.attendees) == 0:
            self.add_players_in_attendees_list(None)
            self.db.update_tournament_in_database(tournament)

    def display_players_list(self, players_list):
        '''Return a list, in case we sort the list'''
        i = 0
        for player in players_list:
            i += 1
            self.view.display_player_to_pick(i, player)

    def add_players_in_attendees_list(self, players_list):
        '''are we on the first attempt of the loop'''
        if players_list is None or len(players_list) == 0:
            players_list = self.db.load_players_list_from_database()

        self.display_players_list(players_list)
        '''refresh the players list to delete the user added'''
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
