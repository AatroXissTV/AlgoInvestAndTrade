# greedy.py
# created 25/10/2021 @14:25
# last updated 25/10/2021 @14:25

"""optimized.py

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
import numpy as np

# local imports
import utils.dataset

# others

"""
This algorithm is by far the best I could think of.
It uses matrices and backtracking to know which wallet is best

Complexity of this algorithm is noted => O(log n)
"""


def optimized(k, items, name, price, profit_percentage):

    # First calculate profit with price & profit_percentage.
    shares_list = utils.dataset.readable_data(name, price,
                                              profit_percentage,
                                              items)

    # Get profit from shares_list:
    profit_int = []
    for share in shares_list:
        share_profit = share[2]
        profit_int.append(share_profit)

    # Phase 1 : Build Grid with best solution

    # Budget updated
    budget = k * 100

    # Initialize Matrice
    matrice = np.empty((items + 1, budget + 1), dtype=int)
    matrice[0] = 0

    for item in range(items):
        this_price = price[item]
        this_value = profit_int[item]
        matrice[item+1, :this_price] = matrice[item, :this_price]
        temp = matrice[item, :-this_price] + this_value
        matrice[item + 1, this_price:] = np.where(
            temp > matrice[item, this_price:], temp, matrice[item, this_price:]
            )

    # Phase 2: Backtracking to get best shares
    wallet_price = 0
    taken = []

    # Backtracking for taken list
    for item in range(items, 0, -1):
        if matrice[item][budget] != matrice[item - 1][budget]:
            taken.append(item - 1)
            budget -= price[item - 1]
            wallet_price += price[item - 1]

    # Display Best Wallet to user
    print("You should buy:")
    profit_total = []
    for item in taken:
        share = shares_list[item]
        # Restore shares to correct prices
        c_s_price = share[1] / 100
        c_s_profit = share[2] / 100

        # Append profit total with profit
        profit_total.append(c_s_profit)

        print(f"{share[0]} for {c_s_price} € -> {c_s_profit} € profit")

    # Restore wallet price & wallet profit
    w_price = wallet_price / 100
    w_profit = sum(profit_total)
    print(f"\nBest Wallet costs {w_price} € -> {w_profit} € profit")
