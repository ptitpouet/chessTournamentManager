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
        self.db = database

    def run(self):
        self.view.show_welcome()
        option = self.view.prompt_for_section()

        if option == 1:
            self.view = TournamentMenuView()
            tournament_management_controller = TournamentManagementController(self.view, self.db)
            tournament_management_controller.run()
        elif option == 2:
            self.view = PlayersMenuView()
            players_controller = PlayersController(self.view, self.db)
            players_controller.run()
        elif option == 3:
            self.view = ReportView()
            report_controller = ReportController(self.view)
            report_controller.run()
        elif option == 4:
            quit()
        else:
            pass
