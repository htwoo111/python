import re

# {m} 匹配前一个字符出现m次
# {m, n} 匹配前一个字符出现m-n次

result = re.match(r"速度与激情\d{0,10}", "速度与激情")
    # {1,3} 表达的是 {}前面的\d 可以有1-3个

print(re.match(r"\d{11}", "12345678901").group())
    # 连续11个，少了不算，而且要连续

print(result.group())

# 匹配前一个字符出现0到1次
print(re.match(r"021-?\d{8}", "021-12345678").group())


# .匹配任意一个字符， 不包括\n（换行）
# *匹配前一个字符任意0-无限个
html_content = """aaaaaa
bbbb
ccc
ddd
"""
print(re.match(r".*", html_content).group())
# re.S 让.包括\n
print(re.match(r".*", html_content, re.S).group())

# +匹配前一个字符1-无限次
print(re.match(r".+", html_content).group())
