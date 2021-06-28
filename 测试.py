# from functools import wraps
#
#
# def beg(target_function):
#     @wraps(target_function)
#     def wrapper(*args, **kwargs):
#         msg, say_please = target_function(*args, **kwargs)
#         print('wrapper')
#         if say_please:
#             return "{} {}".format(msg, "Please! I am poor :(")
#         return msg
#
#     return wrapper
#
#
# @beg
# def say(say_please=False):
#     msg = "Can you buy me a beer?"
#     print('say')
#     return msg, say_please


# print(say())
# print(say(say_please=True))


# from functools import wraps
#
# def test1(A):
#     @wraps(A)
#     def test3():
#        print("I am test3333333")
#     print("I am test1111111111")
#     return test3
#
#
# @test1
# def test2():
#     print("I am test2222222222")
#
#
# test2
# print(test2.__name__)
# test2()
import time


def running_time(func):
    # 内部有新函数
    def print_running_time(*args):
        '''打印函数运行时间'''

        t0 = time.time()
        result = func(*args)
        need_time = time.time() - t0
        print('新列表生成时间（秒）：{:.8f}'.format(need_time))
        return result

    return print_running_time


@running_time
def new_list(n):
    '''生成一个新列表'''
    temp_list = []
    for x in range(n):
        temp_list.append(x * (x + 1))
    return temp_list


if __name__ == "__main__":
    print('新列表长度：{}'.format(len(new_list(12345))))
    print('new_list 函数的 __name__ 属性：{}'.format(new_list.__name__))
    print('new_list 函数的 __doc__ 属性：{}'.format(new_list.__doc__))