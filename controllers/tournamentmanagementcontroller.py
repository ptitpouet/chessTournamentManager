from controllers.tournamentrunnercontroller import TournamentRunnerController
from models.tournament import Tournament
from views.homeview import HomeView
from views.tournamentcreationview import TournamentCreationView
from views.tournamentmenuview import TournamentMenuView
from views.tournamentrunnerview import TournamentRunnerView
from views.tournamentslistview import TournamentsListView


class TournamentManagementController:

    def __init__(self, view, database):
        # views
        self.view = view
        self.db = database

    def run(self):
        self.view.show_welcome()
        option = self.view.prompt_for_section()

        if option == 1:
            self.create_tournament()
        elif option == 2:
            tournaments_list = self.display_tournaments_list()
            self.display_tournaments_list_options(tournaments_list)
        elif option == 3:
            self.back_home()
        else:
            pass

    def back_home(self):
        self.view = HomeView()
        #home_controller = HomeController(self.view, self.db)
        #home_controller.run()

    def display_tournament_menu(self):
        self.view = TournamentMenuView()
        self.run()

    def select_tournament(self, tournaments_list):
        tournament_id = self.view.prompt_for_tournament_id(len(tournaments_list))
        if tournament_id is not None:
            index_tournament_id = tournament_id - 1
            return tournaments_list[index_tournament_id]

    def run_tournament(self, tournament):
        self.view = TournamentRunnerView()
        tournament_runner_controller = TournamentRunnerController(self.view, tournament, self.db)
        tournament_runner_controller.run()

    def launcher_tournament(self, tournaments_list):
        self.display_tournaments_list()
        tournament = self.select_tournament(tournaments_list)
        self.run_tournament(tournament)

    def display_tournaments_list(self):
        self.view = TournamentsListView()

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
                self.display_tournament_menu()
            elif option == 3:
                self.delete_tournament()
                self.display_tournament_menu()
            elif option == 4:
                self.reset_tournaments_database()
            elif option == 5:
                self.display_tournament_menu()
                self.display_tournament_menu()
            else:
                self.display_tournament_menu()
        else:
            self.display_tournament_menu()

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
        self.view = TournamentCreationView()
        self.view.show_welcome()

        #tournaments_list = self.db.load_tournaments_list_from_database()

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
        #tournaments_list.append(tournament)

        self.db.insert_tournament_in_database(tournament)

        if self.view.prompt_for_load_created_tournament():
            self.run_tournament(tournament)
        else:
            self.display_tournament_menu()


