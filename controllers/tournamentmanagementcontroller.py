class TournamentManagementController:

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
            self.create_tournament()
        elif option == 2:
            tournaments_list = self.display_tournaments_list()
            self.display_tournaments_list_options(tournaments_list)
        elif option == 3:
            self.back_home()
        else:
            self.display_menu_options()

    def back_home(self):
        self.controller.home_controller.run()

    def display_tournament_menu(self):
        self.run()

    def select_tournament(self, tournaments_list):
        tournament_id = self.view.prompt_for_tournament_id(len(tournaments_list))
        if tournament_id is not None:
            index_tournament_id = tournament_id - 1
            return tournaments_list[index_tournament_id]

    def run_tournament(self, tournament):
        self.controller.tournament_runner_controller.run(tournament)

    def launcher_tournament(self, tournaments_list):
        self.display_tournaments_list()
        tournament = self.select_tournament(tournaments_list)
        self.run_tournament(tournament)

    def display_tournaments_list(self):
        tournaments_list = self.db.load_tournaments_list_from_database()
        i = 0
        for tournament in tournaments_list:
            i += 1
            self.view.display_tournament(i, tournament)
        return tournaments_list

    def display_tournaments_list_options(self, tournaments_list):
        if len(tournaments_list) > 0:
            option = self.view.prompt_for_list_interaction()
            if option == 1:
                self.launcher_tournament(tournaments_list)
            elif option == 2:
                self.create_tournament()
                self.display_menu_options()
            elif option == 3:
                self.delete_tournament()
                self.display_menu_options()
            elif option == 4:
                self.reset_tournaments_database()
            elif option == 5:
                self.display_menu_options()
            else:
                self.display_menu_options()
        else:
            self.display_menu_options()

    def reset_tournaments_database(self):
        self.db.reset_tournaments_table()

    def delete_tournament(self):
        tournaments_list = self.display_tournaments_list()
        tournament_id = self.view.prompt_for_tournament_id(len(tournaments_list))
        if tournament_id is not None:
            index_tournament_id = tournament_id - 1

            if self.view.prompt_for_tournament_deletion_confirmation(tournaments_list[index_tournament_id]):
                tournaments_list.pop(index_tournament_id)

            self.db.save_tournaments_list_in_database(tournaments_list)
            self.display_tournaments_list()
        else:
            self.display_tournaments_list_options(tournaments_list)

    def create_tournament(self):
        self.controller.tournament_creation_controller.run()
