
profit = float(input("请输入当月利润:"))


reward = [100, 60, 40, 20, 10, 0]
rates = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0

for i in range(0, len(reward)):
    if profit > reward[i]:
        print(profit)
        print(rates[i])
        bonus = bonus + (profit - reward[i]) * rates[i]
        profit = reward[i]

print(bonus)