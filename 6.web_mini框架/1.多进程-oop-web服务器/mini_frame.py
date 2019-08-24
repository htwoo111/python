import time


def login():
    return '-----login----welcome to our websize------time:%s' %time.ctime()

def signout():
    return '-----signout-----%s' %time.ctime()

def register():
    return '-------register------%s' % time.ctime()

def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == '/register.py':
        return register()
    elif file_name == '/signout.py':
        return signout()
    else:
        return 'page not found......'