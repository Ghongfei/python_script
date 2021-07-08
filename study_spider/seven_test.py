from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def func():
    for i in range(100):
        print("func",i)


if __name__ == '__main__':
    t = Thread(target=func)

    t.start()
    for i in range(100):
        print("main",i)