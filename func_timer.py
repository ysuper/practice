import time


class Timer:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        print("{} Start: {}".format(self.name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start))))
        return self

    def __exit__(self, exc, val, traceback):
        self.end = time.time()
        self.spend = time.time() - self.start
        print("{} End  : {}".format(self.name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.end))))
        print("Spend Time : {}".format(self.spend))


def func1():
    s = 0
    for i in range(10000000):
        s += i
    print(s)


with Timer("func1"):
    func1()
