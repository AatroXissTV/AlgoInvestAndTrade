# utils/dataset.py
# created 19/10/2021 @17:36
# last updated 19/10/2O21 @17:36

"""dataset.py

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
import pandas as pd

# local imports

# others

# This file manages all operations on databases


# readable datasets
def readable_data():
    df = pd.read_csv(r'databases/dataset.csv')
    shares_temp = df.values.tolist()

    shares_list = []
    for share in shares_temp:
        name = share[0]
        price = share[1]
        profit_percentage = share[2]
        profit_value = price * (profit_percentage / 100)
        share_correct = [name, price, profit_value]
        shares_list.append(share_correct)
    return shares_list
