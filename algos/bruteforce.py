# bruteforce.py
# created 19/10/2021 @16:01
# last updated 19/10/2O21 @16:01

"""bruteforce.py

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
import itertools
import datetime
from builtins import list

# third-party imports

# local imports
import utils.dataset
import utils.profit

# others

# Bruteforce.py
# This is the easiest way to have best accuracy.
# but this method is not scallable and execution time is really long.


# Determine all combinations for bruteforcing
def determine_all_combinations(shares_list):
    all_combinations = []
    for i in range(len(shares_list) + 1):
        combinations_obj = itertools.combinations(shares_list, i)
        combinations_list = list(combinations_obj)
        all_combinations += combinations_list
    return all_combinations


def bruteforce_algo(all_combinations, k):
    # del first combinations
    del all_combinations[0]

    # Initialize list of all wallet
    all_wallets = []

    # Bruteforce Algo -> calculate all profit
    for i in range(len(all_combinations)):
        current_combination = all_combinations[i]
        w_name, spent, w_profit = create_wallet(current_combination, i, k)
        wallet = [w_name, spent, w_profit]
        all_wallets.append(wallet)

    return all_wallets


# Create a wallet, buy shares and check profit.
def create_wallet(current_combination, i, k):
    wallet_name = i
    amount_spend, wallet_shares_list = buy_shares(current_combination, k)
    wallet_profit = utils.profit.check_profit(wallet_shares_list)
    return wallet_name, amount_spend, wallet_profit


# Buy shares while the budget is not exceeded
def buy_shares(current_combination, k):
    shares_list = []
    amount_spend = 0
    for share in current_combination:
        if (amount_spend + share[1]) <= k:
            amount_spend += share[1]
            shares_list.append(share)
        else:
            pass
    return amount_spend, shares_list


# Determine best wallet
def best_wallet(wallet_lists):
    sorted_w = sorted(wallet_lists, key=lambda w: w[2], reverse=True)
    best_wallet = sorted_w[0]
    return best_wallet


# Bruteforce algorithm
def bruteforce(k):
    # Store begin time for bruteforce algo
    begin_time = datetime.datetime.now()

    # Share list & all combinations
    shares_list = utils.dataset.readable_data()

    all_combinations = determine_all_combinations(shares_list)

    # Bruteforce algo
    all_wallets = bruteforce_algo(all_combinations, k)

    # Determine best wallet
    res = best_wallet(all_wallets)
    end_time = datetime.datetime.now()
    execution_time = end_time - begin_time

    wallet_number = res[0]
    best_wallet_res = all_combinations[wallet_number]

    for item in range(len(best_wallet_res)):
        share = best_wallet_res[item]
        print(f"{share[0]} for {share[1]} that will give you {share[2]}$ ")

    print(f"Best wallet: {res[0]} cost {res[1]}€ gives you {res[2]}€")
    print(f"Took: {execution_time}")
