# 1.property(特性)方法里面只能传一个参数self,多了这个方法就废了
# 2.property方法把一个函数封装并返回一个值，调用的时候不需要加括号，
# 避免传递参数的尴尬


class Goods(object):
    @property
    def size(self):
        return 100


g = Goods()
g.size   # 调用property方法不需要加括号，其方法是返回一个值
# print(g.size)