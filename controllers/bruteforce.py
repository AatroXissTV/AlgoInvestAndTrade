# bruteforce.py
# created 13/10/2021 @16:18
# last updated 13/10/2021 @16:18

"""bruteforce.py

To do:
    * Add tasks
    *
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
import itertools
from builtins import list

# third-party imports

# local imports
from models.shares import Shares
from models.wallet import Wallet

# other


class BruteForce:

    def __init__(self, name):
        self.name = name

    def start_bruteforce(self):
        shares_list = Shares.readable_data()
        all_combinations = BruteForce.determine_all_combinations(shares_list)

        # DEL first combination
        del all_combinations[0]

        # Initialize list of wallets
        wallets_list = []

        for i in range(len(all_combinations)):
            current_combination = all_combinations[i]
            wallet = BruteForce.create_wallet(None, current_combination, i)
            wallet_str = wallet.serialize_wallet()
            wallets_list.append(wallet_str)

        best_wallet = BruteForce.determine_best_profit(wallets_list)
        wallet = Wallet.deserialize_wallet(None, best_wallet[0])
        print(wallet)
        wallet = best_wallet[0]
        get_shares = wallet['shares']
        Shares.getShares(get_shares)

    def determine_best_profit(w_list):
        best_wallet = []
        sorted_w = sorted(w_list, key=lambda w: w['profit'], reverse=True)
        best_wallet.append(sorted_w[0])
        return best_wallet

    def determine_all_combinations(shares_list):
        all_combinations = []
        for i in range(len(shares_list) + 1):
            combinations_obj = itertools.combinations(shares_list, i)
            combinations_list = list(combinations_obj)
            all_combinations += combinations_list
        return all_combinations

    def create_wallet(self, shares_list, i):
        wallet = Wallet(f"my_wallet_{i}")
        wallet_shares_list = wallet.buy_shares(shares_list)
        wallet.check_profit(wallet_shares_list)
        return wallet
