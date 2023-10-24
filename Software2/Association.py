class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = {}

    def buy_stock(self, stock, amount):
        self.stocks[stock.name] = amount

    def sell_stock(self, stock, amount):
        self.stocks.remove(stock)
        self.stocks.remove(amount)

    def print_portfolio(self):
        print(f"Your portfolio {self.name} has following stocks ")
        for x in self.stocks:
            print(f"You have {x} ")


class Stock:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def displ(self):
        print(f"You have {self.name} with value {self.value}")


p = Portfolio("Kimmo's stocks")
s1 = Stock("Nokia",  500)
s2 = Stock("Motorola", 1000)
p.buy_stock(s1, 100)
p.buy_stock(s2, 200)

p2 = Portfolio("Jack's stocks")
p2.buy_stock(s1, 50)
p2.buy_stock(s1, 6)


p.print_portfolio()
s2.displ()
