"""格式"""

# 1.导入模块
import re

# 使用match方法进行匹配操作
# result = re.match()  # (正则表达式， 要匹配的字符串)

re1 = re.match(r"hello", "hello world")

re1.group()