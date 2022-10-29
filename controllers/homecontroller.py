from controllers.playerscontroller import PlayersController
from controllers.reportcontroller import ReportController
from controllers.tournamentcontroller import TournamentController
from views.playersmenuview import PlayersMenuView
from views.reportmenuview import ReportView
from views.tournamentmenuview import TournamentView


class HomeController:

    def __init__(self, view):
        # views
        self.view = view

    def run(self):
        self.view.show_welcome()
        option = self.view.prompt_for_section()

        if option == 1:
            players_view = PlayersMenuView()
            players_controller = PlayersController(players_view)
            players_controller.run()
        elif option == 2:
            tournament_view = TournamentView()
            tournament_controller = TournamentController(tournament_view)
            tournament_controller.run()
        elif option == 3:
            report_view = ReportView()
            report_controller = ReportController(report_view)
            report_controller.run()
        else:
            pass
