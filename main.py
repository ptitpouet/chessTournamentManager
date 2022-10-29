from database import Database
from views.homeview import HomeView
from controllers.homecontroller import HomeController

def main():
    database = Database()
    home_view = HomeView()
    home_controller = HomeController(home_view, database)
    home_controller.run()

if __name__ == '__main__':
    main()
