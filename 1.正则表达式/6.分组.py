import re

email = "14000@qq.com"
# $表示结尾 ^表示开头 (a|b)表示在a/b里面选择
ret = re.match(r"[a-zA-Z_0-9]{4,20}@(163|126|gmail|qq)\.com$", email)

print(ret.group())

# \1  == group(1)
html_str = "<h1>hhhh</h1>"
# ret2 = re.match(r"<(\w*)>.*</\1>", html_str)
# 给分组起名
# (?P<name>)  (?P=name)
ret2 = re.match(r"<(?P<p1>\w*)>.*</(?P=p1)>", html_str)

print(ret2.group())

