class Man:

    def __init__(self, name):
        print('__init__')
        self.name = name

    @property
    def name(self):
        print('property')
        return self._name

    @name.setter
    def name(self, name_value):
        print('setter')
        if not isinstance(name_value, str):
            raise TypeError("Expected a string")
        self._name = name_value  # 需設定另外的變數，通常是加_的私有變數

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


a = Man('ysuper')
print(a.name)
# a.name = 123
a.name = '123'
# del a.name
