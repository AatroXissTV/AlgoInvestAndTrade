# greedy.py
# created 25/10/2021 @14:07
# last updated 25/10/2021 @14:07

"""greedy.py

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

# third-party imports

# local imports
import utils.dataset

# others

"""
This algorithm is a fast and efficient way to determine best wallet.
However, this method is approximative
and does not give the best answer in all cases.

Complexity of this algorithm is noted => O(n log n)
"""


def greedy(k, items, name, price, profit_percentage):

    # First calculate profit with price & profit_percentage.
    shares_list = utils.dataset.readable_data(name, price,
                                              profit_percentage,
                                              items)

    # Sort shares by decreasing profit/price ratio
    sorted_s = sorted(shares_list, key=lambda s: (s[2]/s[1]), reverse=True)

    # Initialize Var
    actualized_budget = k * 100
    wallet_price = 0
    wallet_profit = 0
    shares_list = []
    i = 0

    # Add best share to wallet until wallet_price has reached budget
    while i < len(sorted_s) and wallet_price <= actualized_budget:
        share = sorted_s[i]
        share_price = share[1]
        if wallet_price + share_price <= actualized_budget:
            shares_list.append(share)
            wallet_price = wallet_price + share[1]
            wallet_profit = wallet_profit + share[2]
        i = i+1

    # Display Best Wallet to user
    print("You should buy:")
    for item in range(len(shares_list)):
        share = shares_list[item]

        # Restore shares to correct prices
        c_s_price = share[1] / 100
        c_s_profit = share[2] / 100

        print(f"{share[0]} for {c_s_price} € -> {c_s_profit} € profit")

    # Restore wallet price & wallet profit
    w_price = wallet_price / 100
    w_profit = wallet_profit / 100
    print(f"\nBest Wallet costs {w_price} € -> {w_profit} € profit")
