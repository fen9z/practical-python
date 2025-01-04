# pcost.py
#
# Exercise 1.32(csv moudle)
import csv


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


cost = portFolio_cost("Data/portfolio.csv")
print(f"Total cost", round(cost, 2))
