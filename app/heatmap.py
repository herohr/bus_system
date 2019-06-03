from random import random

from app.models import *

locations = [
    ('丁香宿舍', '34.1207047372,108.8284850121'),
    ('竹园宿舍', '34.1269218732,108.8397073746'),
    ('海棠宿舍', '34.1292842650,108.8344931602'),
    ('丁香食堂', '34.1234225700,108.8296008110'),
    ('竹园食堂', '34.1262646547,108.8385701180'),
    ('海棠食堂', '34.1293197891,108.8341927528'),
    ('A教学楼', '34.1268685854,108.8310170174'),
    ('B教学楼', '34.1259804505,108.8320040703'),
    ('C教学楼', '34.1256429568,108.8331627846'),
    ('D教学楼', '34.1248969134,108.8350939751'),
    ('E教学楼', '34.1246659938,108.8342571259'),
    ('F教学楼', '34.1238844153,108.8372182846'),
    ('G教学楼', '34.1231738830,108.8387632370'),
    ('信远楼', '34.1250212544,108.8389778137'),
    ('工训中心', '34.1263889937,108.8382267952'),
    ('新综', '34.1281297208,108.8365101814'),
    ('老综', '34.1278099981,108.8371968269'),
    ('行政楼', '34.1221436007,108.8383340836'),
    ('家属区', '34.1208823760,108.8289141655'),
    ('北操场', '34.1301190794,108.8307595253'),
    ('南操场', '34.1250923063,108.8275408745'),
    ('大学生活动中心', '34.1269218732,108.8286352158'),
    ('北门', '34.1287869248,108.8375186920'),
    ('东门', '34.1219126737,108.8403725624'),
    ('图书馆', '34.1247725721,108.8328194618'),
]


class Location:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}: {},{}".format(self.name, self.x, self.y)

    @classmethod
    def from_str(cls, name, l):
        x, y = l.split(",")
        return cls(name, float(y), float(x))


locations = [Location.from_str(*i) for i in locations]


def find(location_name):
    for i in locations:
        if location_name == i.name:
            return i
    return None


class Node:
    def __init__(self, location_name, x, y):
        self.name = location_name
        self.x = x
        self.y = y

# nodes


def rand_shake(num):
    v = random()
    shake = (v-0.5) * (10**-3.1)
    return num + shake


def nodes():
    node_list = []
    wjs = WJ.objects.all()
    for i in wjs:
        from_location = find(i.q3)
        to_location = find(i.q4)
        node_list.append(Node(from_location.name, rand_shake(from_location.x), rand_shake(from_location.y)))
        node_list.append(Node(to_location.name, rand_shake(to_location.x), rand_shake(to_location.y)))
    return node_list


def make_js(node_list):
    node_fmt = """"lng": {},"lat": {},"count": 2"""
    nodes_js = ",".join(["{" + node_fmt.format(i.x, i.y) + "}" for i in node_list])
    js = """var heatmapData = [{}];""".format(nodes_js)
    return js


def do():
    return make_js(nodes())

heatmap_js = do()
