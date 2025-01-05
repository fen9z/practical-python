# report.py
#
# Exercise 2.4 a list of tuples
import csv, sys


def read_portfolio(filename):
    """opens a given portfolio file and reads it into a list of tuples."""
    total_cost = 0
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio
