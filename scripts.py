# scripts.py
# created 25/10/2021 @10:36
# last updated 25/10/2021 @10:36

"""scripts.py

To do:
    * Add tasks
    *
"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "2.0.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports
import argparse

# third-party imports

# local imports
import algos.bruteforce as algob
import algos.greedy as algog
import algos.optimized as algoo

# others


if __name__ == '__main__':

    solvers = {
        'bruteforce': algob.bruteforce,
        'greedy': algog.greedy,
        'optimized': algoo.optimized
    }

    parser = argparse.ArgumentParser(
        description="Launch algorithm for AlgoInvest&Trade"
    )

    # Arguments for parser
    parser.add_argument('-f', default='databases/dataset.csv',
                        metavar='filename',
                        help='Name of CSV file (default: %(default)s'
                        'Data format: name, price, value. NO HEADER LINE.')
    parser.add_argument('-b', default=500,
                        metavar='wallet budget',
                        help='choose max budget for a wallet')
    parser.add_argument('algo', choices=list(solvers.keys()),
                        help='Algo implementation choose from %(choices)s')

    args = parser.parse_args()
    verbose = args.v
    datafilename = args.f
    budget = int(args.b)
    launch_algo = solvers[args.algo]

    # Initialize list
    name = []
    price = []
    profit_percentage = []
    items = 0
    item_removed = 0

    with open(datafilename, 'r') as file:
        data = file.read()
    for line in data.split('\n'):
        name_data, price_data, profit_percentage_data = line.split(',')

        # Check if price int is <= 0 or > to budget
        price_int = int(float(price_data))
        if (price_int > budget) or (price_int <= 0):
            item_removed += 1
            pass
        else:
            name.append(name_data)
            price.append(int(float(price_data) * 100))
            profit_percentage.append(int(float(profit_percentage_data) * 100))
            items += 1

    print(f"\n{item_removed} shares removed (null value or budget exceeded)\n")
    launch_algo(budget, items, name, price, profit_percentage)
