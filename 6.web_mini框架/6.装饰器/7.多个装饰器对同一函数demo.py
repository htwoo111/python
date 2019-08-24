def decorator_1(func):
    def call_func():
        return "<h1>" + func() + "</h1>"
    return call_func

def decorator_2(func):
    def call_func():
        return "<body>" + func() + "</body>"
    return call_func

@decorator_2
@decorator_1
def get_str():
    return "hello world"


print(get_str())
