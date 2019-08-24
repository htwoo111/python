class Goods(object):
    
    # 初始化原始价格，和折扣
    def __init__(self, original_price, discount):
        self.original_price = original_price
        self.discount = discount

    @property
    def price(self):
        current_price = self.original_price * self.discount
        return current_price

    @price.setter
    def price(self, value):
        self.original_price = value
    
    @price.deleter
    def price(self):
        del self.original_price


g = Goods(100, 0.8)
print(g.price)
g.price = 200
print(g.price)
del g.price

