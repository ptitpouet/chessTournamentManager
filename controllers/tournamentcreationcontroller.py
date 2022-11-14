from models.tournament import Tournament


class TournamentCreationController:

    def __init__(self, view, controller, database):
        # views
        self.view = view
        self.controller = controller
        self.db = database

    def run(self):
        self.view.show_welcome()

        # tournaments_list = self.db.load_tournaments_list_from_database()

        def get_name():
            name = self.view.prompt_for_tournament_name()
            if name is None:
                get_name()
            else:
                return name

        def get_location():
            location = self.view.prompt_for_tournament_location()
            if location is None:
                get_location()
            else:
                return location

        def get_date():
            date = self.view.prompt_for_tournament_date()
            if date is None:
                get_date()
            else:
                return date

        def get_nb_of_rounds():
            nb_of_rounds = self.view.prompt_for_tournament_nb_of_rounds()
            if nb_of_rounds is None:
                get_nb_of_rounds()
            else:
                return nb_of_rounds

        def get_description():
            description = self.view.prompt_for_tournament_description()
            if description is None:
                get_description()
            else:
                return description

        def get_time_control():
            time_control = self.view.prompt_for_tournament_time_control()
            if time_control is None:
                get_time_control()
            else:
                return time_control

        tournament = Tournament(
            get_name(),
            get_location(),
            get_date(),
            get_nb_of_rounds(),
            get_description(),
            get_time_control()
        )

        self.db.insert_tournament_in_database(tournament)

        if self.view.prompt_for_load_created_tournament():
            self.run_tournament(tournament)
        else:
            self.display_tournament_menu()

    def run_tournament(self, tournament):
        self.controller.tournament_runner_controller.run(tournament)

    def display_tournament_menu(self):
        self.controller.tournament_management_controller.run()
