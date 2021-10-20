# greedy.py
# created 19/10/2021 @17:33
# last updated 19/10/2O21 @17:33

"""greedy.py

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
import datetime

# third-party imports

# local imports
import utils.dataset
import utils.profit

# others

# greedy.py
# This is a fast and efficient way to determine best wallet
# but this method is very approximative and do not deliver best results


# Sort shares list with value/price ratio
def sort_shares_list(shares_list):
    sorted_s = sorted(shares_list, key=lambda s: (s[2]/s[1]), reverse=True)
    return sorted_s


def greedy_algo(sorted_shares, k):
    amount_spend = 0
    shares_list = []
    i = 0
    while i < len(sorted_shares) and amount_spend <= k:
        share = sorted_shares[i]
        price_share = share[1]
        if amount_spend + price_share <= k:
            shares_list.append(share)
            amount_spend = amount_spend + share[1]
        i = i+1
    return shares_list, amount_spend


def greedy(k, items, name, price, profit_percentage):
    # Store begin time for algo
    begin_time = datetime.datetime.now()

    # Wallet name
    w_name = "best_wallet_greedy"

    # Shares list & sorted shares
    shares_list = utils.dataset.readable_data(name, price,
                                              profit_percentage, items)
    sorted_shares = sort_shares_list(shares_list)

    # Greedy algo
    shares, amount_spend = greedy_algo(sorted_shares, k)

    # Determine profit
    profit = utils.profit.check_profit(shares)

    # end time
    end_time = datetime.datetime.now()
    execution_time = end_time - begin_time

    print('you should buy :')
    for share in shares:
        print(f"{share[0]} for {share[1]} that will give you {share[2]}$ ")

    print(f"Best wallet: {w_name} cost {amount_spend}€ gives you {profit}")
    print(f"Took: {execution_time}")
