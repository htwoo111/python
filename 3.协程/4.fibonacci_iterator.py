class Fibonacci(object):
    def __init__(self, length_list):
        # self.nums = list()
        self.length_list = length_list
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.length_list:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration



def main():
    times = int(input("请输入fibonacci数列的长度:"))
    fib = Fibonacci(times)
    # for num in fib:
    #     print(num, end=",")
    print(list(fib))


if __name__ == "__main__":
    main()