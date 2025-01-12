# report.py
#
# Exercise 2.19: List comprehensions

import fileparse


def read_portfolio(filename):
    """opens a given portfolio file and reads it into a list of Dictionaries."""
    portfolio = fileparse.parse_csv(
        filename, select=["name", "shares", "price"], types=[str, int, float]
    )

    return portfolio


def read_prices(filename):
    """reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices."""
    return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))


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


def print_report(report):
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(portfolio_file, prices_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

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

    report = make_report(portfolio, prices)
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit("Usage: %s portfile pricefile" % args[0])
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
