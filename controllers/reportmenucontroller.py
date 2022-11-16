from operator import attrgetter


class ReportMenuController:

    def __init__(self, view, controller, database):
        # views
        self.view = view
        self.controller = controller
        self.db = database

    def run(self):
        self.view.show_welcome()

        self.display_menu_options()

    def display_menu_options(self):
        option = self.view.prompt_for_section()

        if option == 1:
            self.display_all_players_list(self.view.prompt_for_sort_by_rank_or_alphabetic())
            if self.view.prompt_user_to_return():
                self.display_menu_options()
        elif option == 2:
            tournament = self.select_tournament(self.display_tournaments_list())
            self.display_tournament_options(tournament)
        elif option == 3:
            self.back_home()
        else:
            self.display_menu_options()

    def select_tournament(self, tournaments_list):
        tournament_id = self.view.prompt_for_tournament_id(len(tournaments_list))
        if tournament_id is not None:
            index_tournament_id = tournament_id - 1
            return tournaments_list[index_tournament_id]

    def display_tournaments_list(self):
        tournaments_list = self.db.load_tournaments_list_from_database()
        i = 0
        for tournament in tournaments_list:
            i += 1
            self.view.display_tournament(i, tournament)
        return tournaments_list

    def display_tournament_options(self, tournament):
        if tournament is not None:
            option = self.view.prompt_for_list_interaction()
            if option == 1:
                self.report_tournament_players(tournament, self.view.prompt_for_sort_by_rank_or_alphabetic())
                if self.view.prompt_user_to_return():
                    self.display_tournament_options(tournament)
            elif option == 2:
                self.report_tournament_results(tournament)
                if self.view.prompt_user_to_return():
                    self.display_tournament_options(tournament)
            elif option == 3:
                self.display_menu_options()
            else:
                self.display_menu_options()
        else:
            self.display_menu_options()

    def report_tournament_players(self, tournament, sorted_by_rank):
        '''sort players by rank or alphabetic order'''
        if sorted_by_rank is True:
            sorted_list = self.sort_players_by_rank(tournament.attendees)
        else:
            sorted_list = self.sort_players_by_alphabet_order(tournament.attendees)
        ''' display tournament attendees '''
        self.view.display_tournament_attendees(sorted_list)

    def report_tournament_results(self, tournament):
        ''' display all individual matches result '''
        for current_round in tournament.rounds:
            self.view.display_round_details(current_round)

    def back_home(self):
        self.controller.home_controller.run()

    def display_all_players_list(self, sorted_by_rank):
        players_list = self.db.load_players_list_from_database()

        if sorted_by_rank is True:
            players_list = self.sort_players_by_rank(players_list)
            i = 0
            for player in players_list:
                i += 1
                self.view.display_player_with_position(i, player)
        else:
            players_list = self.sort_players_by_alphabet_order(players_list)
            for player in players_list:
                self.view.display_player(player)

    def sort_players_by_alphabet_order(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=attrgetter('lastname', 'firstname', 'birthday'))

    def sort_players_by_rank(self, players_list):
        """ Sort method by score, then rank, then birthday"""
        return sorted(players_list, key=lambda obj: obj.rank)
