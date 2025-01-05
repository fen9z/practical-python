# report.py
#
# Exercise 2.6: Dictionaries as a container

import csv, sys


def read_portfolio(filename):
    """opens a given portfolio file and reads it into a list of Dictionaries."""
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                stock = {
                    "name": row[0],
                    "shares": int(row[1]),
                    "price": float(row[2]),
                }
                portfolio.append(stock)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio


def read_prices(filename):
    """reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices."""
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s["shares"] * s["price"]

print("Total cost", total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s["shares"] * prices[s["name"]]

print("Current value", total_value)
print("Gain", total_value - total_cost)
