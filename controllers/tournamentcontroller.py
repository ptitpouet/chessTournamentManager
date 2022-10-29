from views.homeview import HomeView


class TournamentController:

    def __init__(self, view, database):
        # views
        self.view = view
        self.database = database

    def run(self):
        self.view.show_welcome()
        option = self.view.prompt_for_section()

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            self.display_menu()
        else:
            pass

    def back_home(self):
        self.view = HomeView()
        self.run()