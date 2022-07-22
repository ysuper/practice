class Pair:

    def __init__(self, x, y):
        print("init")
        self.x = x
        self.y = y

    def __repr__(self):
        print("repr")
        return "Pair({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        print("str")
        return "({0.x!s}, {0.y!s})".format(self)


p = Pair(3, 4)
p  # __repr__() output
print(p)  # __str__() output

print("p is {0!r}".format(p))
print("p is {0}".format(p))
