import re

# \d 匹配一个数字
result = re.match(r"速度与激情\d", "速度与激情1")

# 1-8人选一个
result = re.match(r"速度与激情[123456789]", "速度与激情1")
result = re.match(r"速度与激情[1-8]", "速度与激情1") # 数据不连续时不能用
result = re.match(r"速度与激情[1-36-8]", "速度与激情1") # 1-3 and 6-8 不用逗号 可以输入字母
# 中括号里面只匹配一个
result = re.match(r"速度与激情\w", "速度与激情aaa")  # \w 匹配1个word 范围宽广 慎用



print(result.group())