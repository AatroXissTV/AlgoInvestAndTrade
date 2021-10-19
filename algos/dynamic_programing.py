# algos/dynamic_programming.py
# created 19/10/2021 @18:16
# last updated 19/10/2O21 @18:16

"""dynamic_programming.py

To do:
    * Add tasks
    * Need to correct a bug where corrupted data crash the programm
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
import numpy as np
import pandas as pd

# local imports

# others

# dynamic_programming.py
# by far the most efficient way to obtain results

# func bruteforce


# func dynamic programming
def dynamic_programming_algo(budget, items, price, values):

    # Initialize matrice
    matrice = np.empty((items + 1, budget + 1), dtype=int)
    matrice[0] = 0

    for item in range(items):
        this_price = price[item]
        this_value = values[item]
        matrice[item+1, :this_price] = matrice[item, :this_price]
        temp = matrice[item, :-this_price] + this_value
        matrice[item + 1, this_price:] = np.where(
            temp > matrice[item, this_price:], temp, matrice[item, this_price:]
            )

    # Get results
    solution_price = 0
    taken = []
    k = budget

    # Backtracking for results
    for item in range(items, 0, -1):
        if matrice[item][k] != matrice[item - 1][k]:
            taken.append(item - 1)
            k -= price[item - 1]
            solution_price += price[item - 1]

    return solution_price, taken


# return python lists
def return_csv_to_list():
    column_names = ["name", "price", "profit"]
    df = pd.read_csv("databases/dataset.csv", names=column_names)
    name = df.name.to_list()
    price = df.price.to_list()
    profit = df.profit.to_list()
    len_items = len(price)

    return len_items, price, profit, name


# float to int
def convert_float_to_int(list):
    new_list = []
    for item in list:
        new_value = int(item)
        new_list.append(new_value)
    return new_list


def get_profit_value(price, profit):
    i = len(profit)
    profit_values = []
    for item in range(i):
        profit_value = price[item] * (profit[item] / 100)
        profit_values.append(profit_value)

    return profit_values


def dynamic_programming(k):
    begin_time = datetime.datetime.now()
    w_name = "best_wallet_dynamic"
    items, price, profit, name_share = return_csv_to_list()
    profit_values = get_profit_value(price, profit)
    price_list = convert_float_to_int(price)
    profit_list = convert_float_to_int(profit_values)
    amount_spend, taken = dynamic_programming_algo(k, items,
                                                   price_list, profit_list)

    # get shares
    print('you should buy :')
    profit_values = []
    for i in taken:
        name = name_share[i]
        profit_value = price[i] * (profit[i] / 100)
        share_price = price[i]
        profit_values.append(profit_value)
        print(f"{name} for {share_price} that will give you {profit_value}$ ")

    profit_sum = sum(profit_values)

    # end time
    end_time = datetime.datetime.now()
    execution_time = end_time - begin_time

    print(f"Best wallet: {w_name} cost {amount_spend}€ gives you {profit_sum}")
    print(f"Took: {execution_time}")
