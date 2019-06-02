from app.models import *
from random import choice, random
from itertools import product

q2_v = ["ecar", "minubus"]
q3_v = site_names
q4_v = site_names
q5_v = list(product(q3_v, q4_v))


def rand(rate, rs, rs_list):
    if rs is None:
        return choice(rs_list)

    r = random()
    if r < rate:
        return rs
    else:
        return choice(rs_list)


def generate(need):
    while True:
        q1 = True
        q2 = choice(q2_v)
        q3 = rand(0.7, need.q3, q3_v)
        q4 = rand(0.6, need.q4, q4_v)
        q5 = rand(0.5, need.q5, q5_v)
        need = yield q1, q2, q3, q4, q5


# create_wj(True, "ecar", "")
class Need:
    def __init__(self, q3=None, q4=None):
        self.q3 = q3
        self.q4 = q4
        self.q5 = (q3, q4)


def init(need, count):
    a = generate(need)
    print(next(a))
    for i in range(count):
        q1, q2, q3, q4, q5 = a.send(need)
        WJ(q1=q1, q2=q2, q3=q3, q4=q4, q5=",".join(q5)).save()


print(locations)