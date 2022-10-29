from models.tournament import Tournament
from views.homeview import HomeView
from views.tournamentcreationview import TournamentCreationView


class TournamentController:

    def __init__(self, view, database):
        # views
        self.view = view
        self.database = database

    def run(self):
        self.view.show_welcome()
        option = self.view.prompt_for_section()

        if option == 1:
            self.create_tournamen()
        elif option == 2:
            pass
        elif option == 3:
            self.display_menu()
        else:
            pass

    def back_home(self):
        self.view = HomeView()
        self.run()

    def create_tournamen(self):
        self.view = TournamentCreationView()
        self.view.show_welcome()

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
            get_time_control())

        print(str(tournament))