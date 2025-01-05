# report.py
#
# Exercise 2.4 a list of Dictionaries
import csv, sys


def read_portfolio(filename):
    """opens a given portfolio file and reads it into a list of Dictionaries."""
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            try:
                holding = {
                    "name": row[0],
                    "shares": int(row[1]),
                    "price": float(row[2]),
                }
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio
