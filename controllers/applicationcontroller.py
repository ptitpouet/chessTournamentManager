from controllers.databasecontroller import DatabaseController
from controllers.homecontroller import HomeController
from controllers.playercreationcontroller import PlayerCreationController
from controllers.playermenucontroller import PlayerMenuController
from controllers.reportmenucontroller import ReportMenuController
from controllers.tournamentcreationcontroller import TournamentCreationController
from controllers.tournamentmenucontroller import TournamentMenuController
from controllers.tournamentrunnercontroller import TournamentRunnerController
from views.homeview import HomeView
from views.playermenuview import PlayerMenuView
from views.playercreationview import PlayerCreationView
from views.reportmenuview import ReportMenuView
from views.tournamentcreationview import TournamentCreationView
from views.tournamentmenuview import TournamentMenuView
from views.tournamentrunnerview import TournamentRunnerView


class ApplicationController:
    def __init__(self):
        self.db = DatabaseController()
        self.home_controller = HomeController(HomeView(), self, self.db)
        self.tournament_menu_controller = TournamentMenuController(TournamentMenuView(), self, self.db)
        self.tournament_creation_controller = TournamentCreationController(TournamentCreationView(), self, self.db)
        self.tournament_runner_controller = TournamentRunnerController(TournamentRunnerView(), self, self.db)
        self.player_creation_controller = PlayerCreationController(PlayerCreationView(), self, self.db)
        self.player_menu_controller = PlayerMenuController(PlayerMenuView(), self, self.db)
        self.report_menu_controller = ReportMenuController(ReportMenuView(), self, self.db)

    def run(self):
        self.home_controller.run()
