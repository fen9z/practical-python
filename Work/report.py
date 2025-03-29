# report.py
#
# Exercise 4-4: List comprehensions

import fileparse
from stock import Stock
import tableformat


def read_portfolio(filename):
    """opens a given portfolio file and reads it into a list of Dictionaries."""
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )

    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]

    return portfolio


def read_prices(filename):
    """reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices."""
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    reports = []

    for stock in portfolio:
        item = (
            stock.name,
            stock.shares,
            prices[stock.name],
            prices[stock.name] - stock.price,
        )
        reports.append(item)

    return reports


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of(name, shares, price, change) tuples.
    '''
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    # Calculate the total cost of the portfolio
    total_cost = 0.0
    for s in portfolio:
        total_cost += s.shares * s.price

    print("Total cost", total_cost)

    # Compute the current value of the portfolio
    total_value = 0.0
    for s in portfolio:
        total_value += s.shares * prices[s.name]

    print("Current value", total_value)
    print("Gain", total_value - total_cost)

    report = make_report(portfolio, prices)
    #print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 3:
        raise SystemExit("Usage: %s portfile pricefile" % args[0])
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
