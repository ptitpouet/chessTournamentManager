from views.homeview import HomeView
from controllers.homecontroller import HomeController

def main():
    home_view = HomeView()
    home_controller = HomeController(home_view)
    home_controller.run()

if __name__ == '__main__':
    main()
