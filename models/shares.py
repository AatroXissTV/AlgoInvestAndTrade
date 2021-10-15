# shares.py
# created 14/10/2021 @12:42
# last updated 14/10/2021 @12:42

"""shares.py

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


# third-party imports
import pandas as pd

# local imports

# other


class Shares:
    """This class represents all shares
    """

    def readable_data():
        df = pd.read_csv(r'databases/dataset.csv')
        shares = df.values.tolist()

        shares_list = []
        for share in shares:
            share_obj = Share(share[0], share[1], share[2])
            share_str = share_obj.serialize_share()
            shares_list.append(share_str)

        return shares_list

    def getShares(shares_list):
        for share in shares_list:
            share_obj = Share(share['name'], share['price'],
                              share['profit_percentage'])
            print(share_obj)

    def total_price_pool(self, shares_list):
        total_price = 0
        for share in shares_list:
            total_price = total_price + share['price']
        return total_price

    def total_profit(self, shares_list):
        total_profit = 0
        for share in shares_list:
            total_profit = total_profit + share['profit']
        return total_profit

    def sorted_shares_list(self, s_list):
        sorted_s = sorted(s_list, key=lambda s: s['profit_percentage'],
                          reverse=True)
        return sorted_s


class Share:
    """This class represent a share
    """

    def __init__(self, name, price, profit_percentage):
        self.name = name
        self.price = price
        self.profit_percentage = profit_percentage
        self.profit = (self.profit_percentage / 100) * self.price

    def serialize_share(self):
        return {
            'name': self.name,
            'price': self.price,
            'profit_percentage': self.profit_percentage,
            'profit': self.profit
        }

    def deserialize_share(self, data):
        name = data['name']
        price = data['price']
        profit_percentage = data['profit_percentage']
        profit = data['profit']
        return Share(name, price, profit_percentage, profit)

    def __str__(self):
        return ('{}: {}€ / {}% => {}€').format(
            self.name, self.price, self.profit_percentage, self.profit
        )
