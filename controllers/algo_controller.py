# controllers/algo_controllers.py
# created 15/10/2021 @ 15:34 CEST
# last updated 15/10/2021 @ 15:34 CEST

""" controllers/algo_controller.py

To do:
    * Add tasks
    *

"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.2.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports

# third-party imports

# local imports
from views.cli_views import Cli
from views.main_menu import MainMenu
from controllers.bruteforce import BruteForce
from controllers.optimized import Optimized

# other


class AlgoController():
    """this class represents the game controller of AlgoInvest

    Manages main_menu logic
    """

    def __init__(self, app_title):
        """Constructor

        - Args:
            app_title -> str
        """

        self.app_title = app_title

    """Summary of methods and quick explanation

    - start_app(self):
        represents the main menu of the app
    """

    def start_app(self):
        title = self.app_title
        view_menu = MainMenu(app_title=title)

        while (view_menu != 'Quit'):
            Cli.cli_entry(title)
            print("Welcome to AlgoInvest")
            print("You can now determine which shares to buy")
            print("Don't hesitate to give a star on Github\n")
            main_menu = view_menu.main_menu()

            if (main_menu == "launch 'BruteForce' Algorithm"):
                BruteForce.start_bruteforce("BruteForce")
                view_menu.return_to_main()

            elif (main_menu == "launch 'Greedy' Algorithm"):
                Optimized.start_optimized("Greedy")
                view_menu.return_to_main()

            elif (main_menu == "Quit"):
                Cli.cli_clear()
                exit()
