# wallet.py
# created 14/10/2021 @12:12
# last updated 14/10/2021 @12:12

"""wallet.py

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

# third-party importss

# local imports

# other
MAX_BUDGET = 500


class Wallet:
    """This class represent a wallet
    """

    def __init__(self, name, max_budget=MAX_BUDGET):
        self.name = name
        self.max_budget = max_budget
        self.shares = []
        self.amount_spend = 0
        self.profit = 0

    def buy_shares(self, shares):
        for share in shares:
            if (self.amount_spend + share['price']) <= self.max_budget:
                self.amount_spend += share['price']
                self.shares.append(share)
            else:
                print('You have exceeded the maximum budget for your wallet\n')
                return self.shares

    def check_profit(self, shares):
        total_profit = 0
        for share in shares:
            total_profit = total_profit + share['profit']
            self.profit = total_profit
        return self.profit

    def __str__(self):
        return ('\n{} - Budget: {}\nShares: {}\nSpent: {} - Profit {}').format(
            self.name, self.max_budget, self.shares,
            self.amount_spend, self.profit
        )
