class Goods(object):
    
    # 初始化原始价格，和折扣
    def __init__(self, original_price, discount):
        self.original_price = original_price
        self.discount = discount

    def get_price(self):
        """价格描述"""
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    # 采用类方法创建property必须调用property这个类方法
    # 默认参数property(get=None, set=None, del=None, doc=None)
    PRICE = property(get_price, set_price, del_price, True)
    

obj = Goods(100, 0.8)

print(obj.PRICE)
obj.PRICE = 200
print(obj.PRICE.__doc__)
del obj.PRICE