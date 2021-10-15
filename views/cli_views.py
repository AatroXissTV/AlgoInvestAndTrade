# views/cli_views.py
# created 15/10/2021 @ 15:34 CEST
# last updated 15/10/2021 @ 15:34 CEST

""" views/cli_views.py

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
import os

# third-party imports
from pyfiglet import Figlet

# local imports

# other


class Cli():
    """this class represents the command line interface for AlgoInvest
    """

    def __init__(self, app_title):
        """Constructor

        - Args:
            app_title -> str
        """

        self.figlet_font = "doom"
        self.app_title = app_title
        self.title_font = Figlet(font=self.figlet_font)

    """Summary of methods and quick explanation

    - Methods:
        display_title(self):
            display app_title with Figlet

    - ClassMethods:
        cli_entry(title):
            clear screen then calls display_title

        cli_clear(cls):
            clear screen

    """

    def display_title(self) -> str:
        print("{}\n".format(self.title_font.renderText(self.app_title)))

    @staticmethod
    def cli_entry(title):
        view_cli = Cli(app_title=title)
        view_cli.cli_clear()
        view_cli.display_title()

    @classmethod
    def cli_clear(cls):
        os.system('cls')
