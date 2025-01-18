# pcost.py
#
# Exercise 1.33: Reading from the command line


import report


def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = report.read_portfolio(filename)

    return sum([s.shares * s.price for s in portfolio])


def main(argv):
    # deal with pass the name of file in as an argument to a script
    # currently, this file si a script file, it can be recive arguments
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"
    cost = portfolio_cost(filename)
    print(f"Total cost", round(cost, 2))


if __name__ == "__main__":
    import sys

    main(sys.argv)
