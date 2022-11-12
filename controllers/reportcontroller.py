class ReportController:

    def __init__(self, view, controller, database):
        # views
        self.view = view
        self.controller = controller
        self.db = database

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
