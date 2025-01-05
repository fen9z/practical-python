# pcost.py
#
# Exercise 1.33: Reading from the command line

import csv, sys


def portFolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError:
                print("Couldn't parse", row)

    return total_cost


# deal with pass the name of file in as an argument to a script
# currently, this file si a script file, it can be recive arguments
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portFolio_cost(filename)
print(f"Total cost", round(cost, 2))
