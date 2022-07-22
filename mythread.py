from datetime import datetime
import time
import threading
from queue import Queue


def log(name):
    time = datetime.now().strftime('%H:%M:%S')
    log = '[{}]-{}:{}'.format(threading.current_thread().name, name, time)
    print(log)
    return log


def drink(name, q):
    rtn_dict = {}
    rtn_dict['drink-start'] = log('{}:{}-開始'.format(name, drink.__name__))
    time.sleep(2)
    rtn_dict['drink-end'] = log('{}:{}-結束'.format(name, drink.__name__))
    q.put(rtn_dict)


def eat(name, q):
    rtn_dict = {}
    rtn_dict['eat-start'] = log('{}:{}-開始'.format(name, eat.__name__))
    time.sleep(5)
    rtn_dict['eat-end'] = log('{}:{}-結束'.format(name, eat.__name__))
    q.put(rtn_dict)


def run():
    q = Queue()
    s1 = threading.Thread(target=eat, name='y-thread', args=('ysuper', q))
    s2 = threading.Thread(target=drink, name='t-thread', args=('timmy', q))
    threads_list = [s1, s2]
    threads_rtn = []
    for i in range(len(threads_list)):
        threads_list[i].start()
    for i in range(len(threads_list)):
        threads_list[i].join()
    for i in range(len(threads_list)):
        threads_rtn.append(q.get())
    print(threads_rtn)


if __name__ == "__main__":
    run()
