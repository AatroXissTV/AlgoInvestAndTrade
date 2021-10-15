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
__version__ = "0.2.0"
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
        wallet = Wallet("best_wallet")
        sorted_shares = Shares.sorted_shares_list(None, shares_list)
        best_wallet = wallet.greedy_algo(sorted_shares)
        wallet.check_profit(best_wallet)
        print(wallet)
        Shares.getShares(best_wallet)
