from controllers.playerscontroller import PlayersController
from models.match import Match
from models.player import Player
import time
from models.round import Round
from views.homeview import HomeView
from operator import attrgetter
from random import randint
from datetime import datetime

from views.playersmenuview import PlayersMenuView


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
        self.view.display_tournament_players(self.sort_players_by_score_then_rank(self.tournament.attendees))

        for i in range(self.tournament.nb_of_rounds):
            matches = (self.create_matches_of_round(self.tournament))
            current_round = self.run_round("Round " + str(i), matches)
            current_round.matches = matches
            self.tournament.rounds.append(current_round)

        # print(self.create_matches_of_round(self.tournament, False))

    def run_round(self, name, matches):
        new_round = Round(name, time.time(), matches)
        print(str(new_round))
        for match in matches:
            print(name + '|' + str(match))
        return new_round

    def back_to_player_management(self):
        self.view = PlayersMenuView()
        players_controller = PlayersController(self.view, self.db)
        players_controller.run()

    def sort_players_by_alphabet_order(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=attrgetter('lastname', 'firstname', 'birthday'), reverse=True)

    def sort_players_by_score_then_rank(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=attrgetter('score', 'rank', 'birthday'), reverse=True)

    def create_matches_of_round(self, tournament):
        def generate_first_tour_matches_pairs(first_sorted_list):
            """On the 1st round, the list is split in 2 half. 1st player of the first half play with first of 2nd"""
            matches = []
            for i in range(0, int(len(first_sorted_list) / 2), 1):
                matches.append(Match(first_sorted_list[i], first_sorted_list[i + int(len(first_sorted_list) / 2)]))
            return matches
        def generate_following_tour_matches_pairs(following_sorted_list):
            """On the 2nd and following rounds, players play against each other, based on their current score"""
            def has_players_already_played(tournament_to_check, player, opponent):
                has_already_played = False
                for current_round in tournament_to_check.rounds:
                    for current_match in current_round.matches:
                        if current_match.white_player == player and current_match.black_player == opponent:
                            has_already_played = True
                        elif current_match.black_player == player and current_match.white_player == opponent:
                            has_already_played = True
                return has_already_played
            def loop_the_players_list_for_a_match(remaining_sorted_list):
                for j in range(1, len(following_sorted_list), 1):
                    if not has_players_already_played(tournament, following_sorted_list[0],
                                                      following_sorted_list[j]):
                        matches.append(Match(following_sorted_list[0], following_sorted_list[j]))
                        following_sorted_list.pop(j)
                        following_sorted_list.pop(0)
                        return following_sorted_list
                '''Outside the loop'''
                matches.append(Match(following_sorted_list[0], following_sorted_list[1]))
                following_sorted_list.pop(1)
                following_sorted_list.pop(0)
                return following_sorted_list

            matches = []
            while len(following_sorted_list) >= 2:
                loop_the_players_list_for_a_match(following_sorted_list)
            return matches

        sorted_list = self.sort_players_by_score_then_rank(tournament.attendees)
        if tournament.rounds is None or len(tournament.rounds) == 0:
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

        if players_list is None or len(players_list) == 0:
            self.view.display_warning_no_players()
            self.back_to_player_management()
        else:
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
