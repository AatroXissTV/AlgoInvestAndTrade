# bruteforce.py
# created 25/10/2021 @11:32
# last updated 25/10/2021 @11:32

"""bruteforce.py

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
from itertools import combinations
from builtins import list

# third-party imports

# local imports
import utils.dataset

# others


"""
This algorithm is the easiest way to have best accuracy on results.
However, this method is not scallable and execution time is really long
for big amount of data.

Complexity of this algorithm is noted => O(2^n)
"""


def determine_all_combinations(shares_list):
    all_wallet_combinations = []
    for r in range(len(shares_list) + 1):
        combinations_obj = combinations(shares_list, r)
        combinations_list = list(combinations_obj)
        all_wallet_combinations += combinations_list
    return all_wallet_combinations


def bruteforce(k, items, name, price, profit_percentage):

    # First calculate profit with price & profit_percentage.
    shares_list = utils.dataset.readable_data(name, price,
                                              profit_percentage,
                                              items)

    # Determine all combinations of wallets possible
    all_wallet_combinations = determine_all_combinations(shares_list)
    del all_wallet_combinations[0]

    # Initialize list of all wallets
    all_wallets = []

    # Calculate total profit per combination
    for i in range(len(all_wallet_combinations)):
        current_combination = all_wallet_combinations[i]

        # Initialize Var
        wallet_name = i
        wallet_price = 0
        wallet_profit = 0

        # Calculate profit and price
        for share in current_combination:
            wallet_price = wallet_price + share[1]
            wallet_profit = wallet_profit + share[2]

        # Keep only the wallets where wallet_price is inferior to 500 (*100)
        if wallet_price > (k * 100):
            pass
        else:
            wallet = [wallet_name, wallet_price, wallet_profit]
            all_wallets.append(wallet)

    # Determine best wallet
    sorted_w = sorted(all_wallets, key=lambda w: w[2], reverse=True)
    res_wallet = sorted_w[0]
    best_wallet_shares = all_wallet_combinations[res_wallet[0]]

    # Display Best Wallet to user
    print("You should buy:")
    for item in range(len(best_wallet_shares)):
        share = best_wallet_shares[item]

        # Restore shares to correct prices
        c_s_price = share[1] / 100
        c_s_profit = share[2] / 100

        print(f"{share[0]} for {c_s_price} € -> {c_s_profit} € profit")

    # Restore wallet price & wallet profit
    w_price = res_wallet[1] / 100
    w_profit = res_wallet[2] / 100
    print(f"\nBest Wallet costs {w_price} € -> {w_profit} € profit")
