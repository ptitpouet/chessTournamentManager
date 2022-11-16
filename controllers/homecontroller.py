class HomeController:

    def __init__(self, view, controller, database):
        # views
        self.view = view
        self.controller = controller
        self.db = database

    def run(self):
        self.view.show_welcome()
        option = self.view.prompt_for_section()
        if option == 1:
            self.controller.tournament_menu_controller.run()
        elif option == 2:
            self.controller.player_menu_controller.run()
        elif option == 3:
            self.controller.report_menu_controller.run()
        elif option == 4:
            quit()
        else:
            pass
