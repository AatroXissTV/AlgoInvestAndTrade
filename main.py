# main.py
# created 14/10/2021 @12:42
# last updated 14/10/2021 @12:42

"""shares.py

    * Add tasks
"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports


# third-party imports

# local imports
from controllers.bruteforce import BruteForce


# other

def main():
    """Is the entry point for the app
    """

    launch_app = BruteForce("bruteforce")
    launch_app.start_bruteforce()


main()
