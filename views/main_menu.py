# views/main_menu.py
# created 15/10/2021 @ 16:12 CEST
# last updated 15/10/2021 @ 16:12 CEST

# must be at the beginning of the file
from __future__ import print_function, unicode_literals

""" views/main_views.py

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
from PyInquirer import style_from_dict, Token, prompt

# local imports
from views.cli_views import Cli

# other


class MainMenu(Cli):
    """This class represents the main menu of AlgoInvest

    - Herit from Cli (cli_views.py)
    """

    def __init__(self, app_title):
        super().__init__(app_title)
        """Constructor

        app_title -> str
        """

        self.style = style_from_dict({
            Token.Answer: '#568259',
            Token.Question: '',  # Default
            Token.Instruction: '#E63946',
            Token.Pointer: '#F1FAEE'
        })

        self.main_menu_form = [
            {
                'type': 'list',
                'name': 'main_menu',
                'message': "Select: ",
                'choices': ["launch 'BruteForce' Algorithm",
                            "launch 'Greedy' Algorithm",
                            "Quit"]
            }
        ]

        self.return_to_main_form = [
            {
                'type': 'confirm',
                'name': 'return_main',
                'message': 'do you want to return to main menu?',
                'default': False
            }
        ]

    """Summary of methods and quick explanation

    - Methods:
        main_menu(self):
            used to prompt main_menu_form
            Return a dict() of the answer
    """

    def main_menu(self):
        main_menu = self.main_menu_form
        answers = prompt(main_menu, style=self.style)
        return answers['main_menu']

    def return_to_main(self):
        return_to_main = self.return_to_main_form
        answers = prompt(return_to_main, style=self.style)
        return answers
