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

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                stock = {
                    "name": record["name"],
                    "shares": int(record["shares"]),
                    "price": float(record["price"]),
                }
                portfolio.append(stock)
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")

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


def make_report(portfolio, prices):
    reports = []

    for stock in portfolio:
        item = (
            stock["name"],
            stock["shares"],
            prices[stock["name"]],
            prices[stock["name"]] - stock["price"],
        )
        reports.append(item)

    return reports


portfolio = read_portfolio("Data/portfolio.csv")
portfoliodate = read_portfolio("Data/portfoliodate.csv")
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


print("\nportfolio.csv report\n")
report1 = make_report(portfolio, prices)

# Output the report1
headers = ("Name", "Shares", "Price", "Change")
print("%10s %10s %10s %10s" % headers)
print(("-" * 10 + " ") * len(headers))
for name, shares, price, change in report1:
    print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")

print("\nportfoliodate.csv report\n")
report2 = make_report(portfoliodate, prices)

# Output the report2
headers = ("Name", "Shares", "Price", "Change")
print("%10s %10s %10s %10s" % headers)
print(("-" * 10 + " ") * len(headers))
for name, shares, price, change in report2:
    print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")
