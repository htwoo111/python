import re

def main():
    names = ["age", "_age", "1age", "a_age", "age_1_", "a#123", "age!"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_]+$", name)
        if ret:
            print("变量名{}，符合要求,通过正则匹配的是{}".format(name, ret.group()))
        else:
            print("变量名{}，不符合要求！！！！".format(name))
            


if __name__ == "__main__":
    main()