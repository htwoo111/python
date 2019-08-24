import re


def main():
    emails = ["1450111@163.com",
              "das11114@163.com",
              "1@163.com"
              "2323sdds@163.com",
              "啊啊的阿萨555@163.com",
              "sdddddddd",
              "@!afdas@163.com",
              "aaaa@163.commmm"]
    for email in emails:
        # 如果在正则表达式中需要用到某些普通的字符，比如，.?等，需要在前面加\转义
        ret = re.match(r"^[a-zA-Z0-9_]{4,20}@163\.com$", email)
        if ret:
            print("email：{}符合要求".format(email))
        else:
            print("email:{}不符合要求！！！！".format(email))



if __name__ == "__main__":
    main()