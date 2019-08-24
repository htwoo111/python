class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs): # __new__(cls, "User", , {"uid":('uid', "int unsigned").... }
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的实例对象
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除这些已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        # -------------attrs-------------------
        # {'__module__': '__main__',
        #  '__qualname__': 'User',
        #   '__init__': <function User.__init__ at 0x03E46F60>,
        #    'save': <function User.save at 0x04713108>,
        #     '__mappings__': {'uid': ('uid', 'int unsigned'),'name': ('username', 'varchar(30)'),'email': ('email', 'varchar(30)'),'password': ('password', 'varchar(30)')},
        #         '__table__': 'User'}
        return type.__new__(cls, name, bases, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")
    # 当指定元类之后，以上的类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 以上User类中有 
    # __mappings__ = {
    #     "uid": ('uid', "int unsigned")
    #     "name": ('username', "varchar(30)")
    #     "email": ('email', "varchar(30)")
    #     "password": ('password', "varchar(30)")
    # }
    # __table__ = "User"
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        # ------结果为------
        # self.uid = 12345
        # self.name = "Michael"
        # self.email = "test@orm.org"
        # self.password = "my-pwd"

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])  # fields = ["uid", "username", "email", "password"]
            args.append(getattr(self, k, None)) # args = [self.iud, self.name, self.email, self.password]

        temp_args = list()
        for temp in args:
            if isinstance(temp, int):
                temp_args.append(str(temp))
            elif isinstance(temp, str):
                temp2 = """'%s'""" % temp
                temp_args.append(temp2)
        sql = """insert into %s (%s) values (%s)""" % (self.__table__, ','.join(fields), ','.join(temp_args))
        # sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
# print(u.__dict__)
u.save()

