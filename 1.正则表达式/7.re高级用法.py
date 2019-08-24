import re

# search 不从开始匹配，只匹配一次
ret = re.search(r"\d+", "阅读次数：9999， 点赞：888")
# 返回一个列表，不需要用group()
ret1 = re.findall(r"\d+", "阅读次数：9999， 点赞：888")

# 将匹配到的所有！！内容替换 然后返回整个内容
ret2 = re.sub(r"\d+", "7777", "阅读次数：9999， 点赞：888")

# 切割字符串， 返回一个列表
ret3 = re.split(r":| ", "info:1111 小米 guangdong")

print(ret.group())
print(ret1)
print(ret2)
print(ret3)