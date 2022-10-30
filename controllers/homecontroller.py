from controllers.playerscontroller import PlayersController
from controllers.reportcontroller import ReportController
from controllers.tournamentmanagementcontroller import TournamentManagementController
from views.playersmenuview import PlayersMenuView
from views.reportmenuview import ReportView
from views.tournamentmenuview import TournamentMenuView


class HomeController:

    def __init__(self, view, database):
        # views
        self.view = view
        self.database = database

    def run(self):
        self.view.show_welcome()
        option = self.view.prompt_for_section()

        if option == 1:
            tournament_view = TournamentMenuView()
            tournament_management_controller = TournamentManagementController(tournament_view, self.database)
            tournament_management_controller.run()
        elif option == 2:
            players_view = PlayersMenuView()
            players_controller = PlayersController(players_view, self.database)
            players_controller.run()
        elif option == 3:
            report_view = ReportView()
            report_controller = ReportController(report_view)
            report_controller.run()
        elif option == 4:
            quit()
        else:
            pass
