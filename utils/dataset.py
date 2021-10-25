# utils/dataset.py
# created 19/10/2021 @17:36
# last updated 25/10/2O21 @11:55

"""dataset.py

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

# others

# This file manages all operations on databases


# readable dataset
def readable_data(name, price, profit_percentage, items):

    shares_list = []

    for i in range(items):
        profit_value = int(price[i] * (profit_percentage[i] / 10000))
        share = [name[i], price[i], profit_value]
        shares_list.append(share)

    return shares_list
