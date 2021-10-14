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
        wallet = Wallet("my_wallet")
        wallet_shares_list = wallet.buy_shares(shares_list)
        wallet.check_profit(wallet_shares_list)
        print(wallet)
