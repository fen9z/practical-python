# pcost.py
#
# Exercise 1.27, 1.30, 1.31(error handle)


def portFolio_cost(filename):
    f = open(filename, "rt")
    headers = next(f).split(",")
    cost = 0

    for line in f:
        fields = line.split(",")
        try:
            shares = int(fields[1])
            price = float(fields[2])
            cost += shares * price
        except ValueError:
            print("Couldn't parse", line)

    return cost


cost = portFolio_cost("Data/portfolio.csv")
print(f"Total cost", round(cost, 2))
