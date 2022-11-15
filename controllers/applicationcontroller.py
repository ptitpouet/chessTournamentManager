from controllers.databasecontroller import DatabaseController
from controllers.homecontroller import HomeController
from controllers.playercreationcontroller import PlayerCreationController
from controllers.playermanagementcontroller import PlayerManagementController
from controllers.reportmanagementcontroller import ReportManagementController
from controllers.tournamentcreationcontroller import TournamentCreationController
from controllers.tournamentmanagementcontroller import TournamentManagementController
from controllers.tournamentrunnercontroller import TournamentRunnerController
from views.homeview import HomeView
from views.playermanagementview import PlayerManagementView
from views.playercreationview import PlayerCreationView
from views.reportmanagementview import ReportManagementView
from views.tournamentcreationview import TournamentCreationView
from views.tournamentmanagementview import TournamentManagementView
from views.tournamentrunnerview import TournamentRunnerView


class ApplicationController:
    def __init__(self):
        self.db = DatabaseController()
        self.home_controller = HomeController(HomeView(), self, self.db)
        self.tournament_management_controller = TournamentManagementController(TournamentManagementView(), self, self.db)
        self.tournament_creation_controller = TournamentCreationController(TournamentCreationView(), self, self.db)
        self.tournament_runner_controller = TournamentRunnerController(TournamentRunnerView(), self, self.db)
        self.player_creation_controller = PlayerCreationController(PlayerCreationView(), self, self.db)
        self.player_management_controller = PlayerManagementController(PlayerManagementView(), self, self.db)
        self.report_management_controller = ReportManagementController(ReportManagementView(), self, self.db)

    def run(self):
        self.home_controller.run()
