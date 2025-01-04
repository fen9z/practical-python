# pcost.py
#
# Exercise 1.33(csv moudle)
import csv, sys


def portFolio_cost(filename):
    f = open(filename, "rt")
    rows = csv.reader(f)
    headers = next(rows)
    cost = 0

    for row in rows:
        try:
            shares = int(row[1])
            price = float(row[2])
            cost += shares * price
        except ValueError:
            print("Couldn't parse", row)

    return cost


# deal with pass the name of file in as an argument to a script
# currently, this file si a script file, it can be recive arguments
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portFolio_cost(filename)
print(f"Total cost", round(cost, 2))
