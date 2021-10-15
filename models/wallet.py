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
__version__ = "0.1.0"
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

    def __init__(self, name, max_budget=MAX_BUDGET,
                 amount_spend=0, profit=0):
        self.name = name
        self.max_budget = max_budget
        self.shares = []
        self.amount_spend = amount_spend
        self.profit = profit

    def serialize_wallet(self):
        return {
            'name': self.name,
            'max_budget': self.max_budget,
            'shares': self.shares,
            'amount_spend': self.amount_spend,
            'profit': self.profit
        }

    def buy_shares(self, shares):
        for share in shares:
            if (self.amount_spend + share['price']) <= self.max_budget:
                self.amount_spend += share['price']
                self.shares.append(share)
            else:
                pass
        return self.shares

    def greedy_algo(self, sorted_s_list):
        i = 0
        while i < len(sorted_s_list) and self.amount_spend <= self.max_budget:
            share = sorted_s_list[i]
            price_share = share['price']
            if self.amount_spend + price_share < self.max_budget:
                self.shares.append(share)
                self.amount_spend = self.amount_spend + share['price']
            i = i+1
        return self.shares

    def check_profit(self, shares):
        total_profit = 0
        for share in shares:
            total_profit = total_profit + share['profit']
            self.profit = total_profit
        return self.profit

    def deserialize_wallet(self, data):
        name = data['name']
        max_budget = data['max_budget']
        amount_spend = data['amount_spend']
        profit = data['profit']
        return Wallet(name, max_budget, amount_spend, profit)

    def __str__(self):
        return ('\n{} - Budget: {}\nSpent: {} - Profit {}').format(
            self.name, self.max_budget,
            self.amount_spend, self.profit
        )
