import random

from . import my_headers


def get_header():

    # 随机提取一个user-agent
    return random.choice(my_headers)