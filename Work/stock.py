# stock

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price
    
    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares


class MyStock(Stock):
    def __init__(self, name, shares, price, factor) -> None:
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        return 1.25 * super().cost()
    