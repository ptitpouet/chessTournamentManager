class TournamentController:

    def __init__(self, view):
        # views
        self.view = view

    def run(self):
        self.view.show_welcome()

        option = self.view.prompt_for_section()

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        else:
            pass