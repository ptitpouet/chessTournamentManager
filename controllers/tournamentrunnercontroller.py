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

        if self.tournament.rounds is None or len(self.tournament.rounds) == 0 :
            self.tournament.rounds = self.create_tournament_rounds(self.tournament.nb_of_rounds)
        else:
            if self.view.prompt_for_tournament_reset() :
                self.tournament.rounds = self.create_tournament_rounds(self.tournament.nb_of_rounds)

        for i in range(len(self.tournament.rounds)):
            if not self.tournament.rounds[i].is_finished:
                self.run_round(i, self.tournament)
                self.db.update_tournament_in_database(self.tournament)

        self.display_tournament_results(self.tournament)


    def display_tournament_results(self, tournament):
        self.view.display_tournament_overall_ranking(self.tournament)
        for current_round in tournament.rounds:
            self.view.display_all_match_results(current_round)

    def create_tournament_rounds(self, nb_of_rounds):
        rounds = []
        for i in range(nb_of_rounds):
            rounds.append(Round("Round " + str(i + 1), None, None, False))
        return rounds

    def run_round(self, round_position, tournament):
        tournament.rounds[round_position].start_round(time.time(),
                                                      self.create_matches_of_round(round_position, tournament))
        self.view.display_round_details(tournament.rounds[round_position])
        for match in tournament.rounds[round_position].matches:
            if not match.is_finished:
                self.collect_match_winner(match)
                self.db.update_tournament_in_database(self.tournament)
        tournament.rounds[round_position].close_round(time.time())

    def collect_match_winner(self, match):
        winner_input = self.view.prompt_for_match_result(match)
        if winner_input == 0:
            print(match.update_score(None))
        elif winner_input == 1:
            print(match.update_score(match.white_player))
        elif winner_input == 2:
            print(match.update_score(match.black_player))
        else:
            self.collect_match_winner(match)

    def back_to_player_management(self):
        self.view = PlayersMenuView()
        players_controller = PlayersController(self.view, self.db)
        players_controller.run()

    def sort_players_by_alphabet_order(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=attrgetter('lastname', 'firstname', 'birthday'))

    def sort_players_by_score_then_rank(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=lambda obj: (-obj.score, obj.rank))

    def create_matches_of_round(self, round_position, tournament):
        def generate_first_tour_matches_pairs(first_sorted_list):
            """On the 1st round, the list is split in 2 half. 1st player of the first half play with first of 2nd"""
            matches = []
            for i in range(0, int(len(first_sorted_list) / 2), 1):
                matches.append(Match(first_sorted_list[i], first_sorted_list[i + int(len(first_sorted_list) / 2)], False))
            return matches

        def generate_following_tour_matches_pairs(following_sorted_list):
            """On the 2nd and following rounds, players play against each other, based on their current score"""
            def has_players_already_played(tournament_to_check, player, opponent):
                has_already_played = False
                for current_round in tournament_to_check.rounds:
                    if current_round.matches is not None:
                        for current_match in current_round.matches:
                            if current_match.white_player == player and current_match.black_player == opponent:
                                has_already_played = True
                            elif current_match.black_player == player and current_match.white_player == opponent:
                                has_already_played = True
                return has_already_played

            def loop_the_players_list_for_a_match(remaining_sorted_list):
                for j in range(1, len(remaining_sorted_list), 1):
                    if not has_players_already_played(tournament, remaining_sorted_list[0],
                                                      remaining_sorted_list[j]):
                        matches.append(Match(remaining_sorted_list[0], remaining_sorted_list[j], False))
                        remaining_sorted_list.pop(j)
                        remaining_sorted_list.pop(0)
                        return remaining_sorted_list
                '''Outside the loop'''
                matches.append(Match(remaining_sorted_list[0], remaining_sorted_list[1], False))
                remaining_sorted_list.pop(1)
                remaining_sorted_list.pop(0)
                return remaining_sorted_list

            matches = []
            while len(following_sorted_list) >= 2:
                loop_the_players_list_for_a_match(following_sorted_list)
            return matches

        sorted_list = self.sort_players_by_score_then_rank(tournament.attendees)
        if round_position == 0:
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

        if len(players_list)>0 and self.view.prompt_for_add_another_player():
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
