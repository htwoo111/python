import re


file_name = "/dsadas.html"
dic =  {
              r"/index.html":'index',
              r"/center.html":'center',
              r"/add/\d+\.html":'add_focus'
            }


def test():
    for url, func in dic.items():
        ret = re.match(url, file_name)
        if ret:
            return 1
    else:
        return "请求的url(%s)没有对应的函数" % url

result = test()
print(result)