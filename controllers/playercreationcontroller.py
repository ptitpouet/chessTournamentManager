from models.player import Player


class PlayerCreationController:

    def __init__(self, view, controller, database):
        # views
        self.view = view
        self.controller = controller
        self.db = database

    def run(self):
        self.view.show_welcome()

        def get_last_name():
            last_name = self.view.prompt_for_last_name()
            if last_name is None:
                get_last_name()
            else:
                return last_name

        def get_first_name():
            first_name = self.view.prompt_for_first_name()
            if first_name is None:
                get_first_name()
            else:
                return first_name

        def get_birthday():
            birthday = self.view.prompt_for_birthday()
            if birthday is None:
                get_birthday()
            else:
                return birthday

        def get_gender():
            gender = self.view.prompt_for_gender()
            if gender is None:
                get_gender()
            else:
                return gender

        def get_rank():
            rank = self.view.prompt_for_rank()
            if rank is None:
                get_rank()
            else:
                return rank

        player = Player(get_last_name(), get_first_name(), get_birthday(), get_gender(), get_rank())

        self.db.insert_player_in_database(player)

        if self.view.prompt_for_another_player():
            self.run()
        else:
            self.controller.player_management_controller.run()
