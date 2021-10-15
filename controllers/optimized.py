# optimized.py
# created 15/10/2021 @11:43
# last updated 15/10/2021 @11:43

"""optimized.py

To do:
    * Add tasks
    *
"""

__author__ = "Antoine 'AatroXiss' BEAUDESSON"
__copyright__ = "2021 Aatroxiss <antoine.beaudesson@gmail.com>"
__credits__ = ["Antoine 'AatroXiss' BEAUDESSON"]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Antoine 'AatroXiss' BEAUDESSON"
__email__ = "<antoine.beaudesson@gmail.com>"
__status__ = "Student in Python"

# standard imports

# third-party imports

# local imports
from models.shares import Shares
from models.wallet import Wallet

# other


class Optimized:

    def __init__(self, name) -> None:
        self.name = name

    def start_optimized(self):
        shares_list = Shares.readable_data()
        print(shares_list)
        sorted_s = Optimized.order_profit_percentage(shares_list)
        best_profit = Optimized.determine_best_profit(sorted_s, 1)
        print(best_profit)

    def order_profit_percentage(s_list):
        sorted_s = sorted(s_list, key=lambda s: s['profit_percentage'],
                          reverse=True)
        return sorted_s

    def determine_best_profit(sorted_shares, i):
        wallet = Wallet(f"my_wallet_{i}")
        wallet_shares_list = wallet.buy_shares(sorted_shares)
        Shares.getShares(wallet_shares_list)
        wallet.check_profit(wallet_shares_list)
        return wallet
