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
import argparse

# third-party imports

# local imports
import algos.bruteforce
import algos.greedy
import algos.dynamic_programing

# others


if __name__ == '__main__':

    solvers = {
        'bruteforce': algos.bruteforce.bruteforce,
        'greedy': algos.greedy.greedy,
        'dynamic_programming': algos.dynamic_programing.dynamic_programming,
    }

    parser = argparse.ArgumentParser(
        description="Launch one algorithm for AlgoInvest"
    )
    parser.add_argument('-v', action='store_true', default=False,
                        help='Verbose Output.')
    parser.add_argument('-f', default='dataset.csv', metavar="filename",
                        help='Name of CSV data file (default: %(default)s'
                        'Data format: name, price, value. No header line.')
    parser.add_argument('-b', default=500, metavar='wallet budget',
                        help="Wallet max budget")
    parser.add_argument('algo', choices=list(solvers.keys()),
                        help="Algo implementation. Choose from %(choices)s")

    args = parser.parse_args()
    verbose = args.v
    datafilename = args.f
    budget = int(args.b)
    solver = solvers[args.algo]

    name = []
    price = []
    profit = []
    items = 0

    with open(f"databases/{datafilename}", 'r') as file:
        data = file.read()
    for line in data.split('\n'):
        name_d, price_d, profit_d = line.split(',')
        name.append(name_d)
        price.append(int(float(price_d)))
        profit.append(int(float(profit_d)))
        items += 1

    solver(budget, items, name, price, profit)
