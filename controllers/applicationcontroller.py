from controllers.databasecontroller import DatabaseController
from controllers.homecontroller import HomeController
from controllers.playerscontroller import PlayersController
from controllers.reportcontroller import ReportController
from controllers.tournamentmanagementcontroller import TournamentManagementController
from views.homeview import HomeView
from views.playersmenuview import PlayersMenuView
from views.reportmenuview import ReportView
from views.tournamentmenuview import TournamentMenuView


class ApplicationController:
    def __init__(self):
        self.db = DatabaseController()
        self.home_controller = HomeController(HomeView(), self, self.db)
        self.tournament_management_controller = TournamentManagementController(TournamentMenuView(), self, self.db)
        self.players_controller = PlayersController(PlayersMenuView(), self, self.db)
        self.report_controller = ReportController(ReportView(), self, self.db)

    def run(self):
        self.home_controller.run()
