# scripts.py
# created 19/10/2021 @16:01
# last updated 19/10/2O21 @16:01

"""scripts.py

To do:
    * Add tasks
    *
"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports


# third-party imports

# local imports
import algos.bruteforce
import algos.greedy
import algos.dynamic_programing

# others
MAX_BUDGET = 500

# Scripts for AlgoInvest&Trade
# 3 different algorithms


# Entry Point
def main():
    print('Launching Bruteforce')
    algos.bruteforce.bruteforce(MAX_BUDGET)
    print("\n")
    print('launching Greedy algorithm')
    algos.greedy.greedy(MAX_BUDGET)
    print("\n")
    print("Launching Dynamic programming algo")
    algos.dynamic_programing.dynamic_programming(MAX_BUDGET)


main()
