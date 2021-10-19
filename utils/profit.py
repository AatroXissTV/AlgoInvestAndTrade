# utils/profit.py
# created 19/10/2021 @18:13
# last updated 19/10/2O21 @18:13

"""scripts.py

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


# third-party imports

# local imports

# others


# check profit of a wallet
def check_profit(wallet_shares_list):
    total_profit = 0
    for share in wallet_shares_list:
        total_profit = total_profit + share[2]
    return total_profit
