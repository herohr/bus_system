from copy import deepcopy, copy
from itertools import product


class TSP:
    def __init__(self, locations):
        self.locations = locations
        self.c = self.dis_mat(locations)
        self.path_length = []
        self.path_vertexs = []
        self.result = self.get_path(*self.find_path(0))

    def find_path(self, j):
        self.path_vertexs.append(j)  # 把该节点标记为已走过
        row = self.c[j]
        # 创建copy_row,删除row中已走过的顶点,防止直接在row上操作.
        copy_row = [value for value in row]
        walked_vertex = []
        for i in self.path_vertexs:  # 已走过的顶点
            walked_vertex.append(copy_row[i])
        for vertex in walked_vertex:
            copy_row.remove(vertex)
        # 寻找row中的未遍历过的最短边
        if len(self.path_vertexs) < len(self.locations):
            min_e = min(copy_row)
            j = row.index(min_e)
            self.path_length.append(min_e)
            self.find_path(j)
        else:
            min_e = self.c[j][0]
            self.path_length.append(min_e)
            self.path_vertexs.append(0)
        return self.path_vertexs, self.path_length

    def get_path(self, vertexs, lengths):
        path = []
        vertexs = [vertex + 1 for vertex in vertexs]
        for i, vertex in enumerate(vertexs):
            path.append(self.locations[vertex - 1])
            if i == len(self.c):
                break
        print("路 径：", path)
        return path

    def dis_mat(self, locations):
        mat = [[0] * len(locations) for i in range(len(locations))]
        p = product(locations, locations)
        row_count = 0
        col_count = 0
        for i in p:
            # a = Location.from_str(*i[0])
            # b = Location.from_str(*i[1])
            dis = self.get_dis(i[0], i[1])
            mat[row_count][col_count] = dis
            col_count += 1
            if col_count % len(locations) == 0:
                row_count += 1
                col_count = 0
        for i in mat:
            print(i)
        return mat

    @staticmethod
    def get_dis(a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


# _locations = [
#     ('丁香宿舍', '34.1240798106,108.8290965557'),
#     ('竹园宿舍', '34.1269218732,108.8397073746'),
#     ('海棠宿舍', '34.1290800006,108.8334202766'),
#     ('ABC教学楼', '34.1268685854,108.8310170174'),
#     ('DEFG教学楼', '34.1245727376,108.8366818428'),
#     ('信远楼', '34.1250212544,108.8389778137'),
#     ('综合楼', '34.1281297208,108.8365101814'),
#     ('家属区', '34.1210333687,108.8312208652'),
#     ('北操场', '34.1286537082,108.8307648897'),
#     ('南操场', '34.1250923063,108.8275408745'),
#     ('北门', '34.1287869248,108.8375186920'),
#     ('家属区与远望谷', '34.1203761044,108.8363385201'),
#     ('图书馆', '34.1240709290,108.8330125809'),
#     ('东门', '34.1223789680,108.8400292397'),
# ]


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


def generate_circle_path():
    circle_locations = [
        ('礼仪广场D楼', '34.1251722397,108.8352441788'),
        ('东门', '34.1223789680,108.8400292397'),
        ('丁香宿舍', '34.1240798106,108.8290965557'),
        ('竹园宿舍', '34.1269218732,108.8397073746'),
        ('海棠宿舍', '34.1290800006,108.8334202766'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('EFG教学楼', '34.1240886922,108.8378190994'),
        ('信远楼', '34.1250212544,108.8389778137'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('家属区', '34.1210333687,108.8312208652'),
        ('北操场', '34.1286537082,108.8307648897'),
        ('南操场', '34.1251455952,108.8286459446'),
        ('北门', '34.1287869248,108.8375186920'),
        ('家属区与远望谷', '34.1203761044,108.8363385201'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return TSP(locations)


def generate_part_E():
    circle_locations = [
        ('礼仪广场D楼', '34.1251722397,108.8352441788'),
        ('东门', '34.1223789680,108.8400292397'),
        ('竹园宿舍', '34.1269218732,108.8397073746'),
        ('EFG教学楼', '34.1240886922,108.8378190994'),
        ('信远楼', '34.1250212544,108.8389778137'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        # ('综合楼', '34.1281297208,108.8365101814'),
        # ('北门', '34.1287869248,108.8375186920'),
        ('家属区与远望谷', '34.1203761044,108.8363385201'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return TSP(locations)


def generate_part_W():
    circle_locations = [
        ('礼仪广场D楼', '34.1251722397,108.8352441788'),
        ('丁香宿舍', '34.1240798106,108.8290965557'),
        ('海棠宿舍', '34.1290800006,108.8334202766'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('家属区', '34.1210333687,108.8312208652'),
        ('北操场', '34.1286537082,108.8307648897'),
        ('南操场', '34.1251455952,108.8286459446'),
        ('北门', '34.1287869248,108.8375186920'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return TSP(locations)


def generate_part_N():
    circle_locations = [
        ('礼仪广场D楼', '34.1251722397,108.8352441788'),
        ('东门', '34.1223789680,108.8400292397'),
        ('竹园宿舍', '34.1269218732,108.8397073746'),
        ('海棠宿舍', '34.1290800006,108.8334202766'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('EFG教学楼', '34.1240886922,108.8378190994'),
        ('信远楼', '34.1250212544,108.8389778137'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('北操场', '34.1286537082,108.8307648897'),
        ('北门', '34.1287869248,108.8375186920')
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return TSP(locations)


def generate_part_S():
    circle_locations = [
        ('礼仪广场D楼', '34.1251722397,108.8352441788'),
        ('东门', '34.1223789680,108.8400292397'),
        ('丁香宿舍', '34.1240798106,108.8290965557'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('EFG教学楼', '34.1240886922,108.8378190994'),
        ('家属区', '34.1210333687,108.8312208652'),
        ('南操场', '34.1251455952,108.8286459446'),
        ('家属区与远望谷', '34.1203761044,108.8363385201'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return TSP(locations)


# print(locations)

pathC = generate_circle_path()  # 外环线
pathE = generate_part_E()
pathW = generate_part_W()
pathN = generate_part_N()
pathS = generate_part_S()
for i in [('礼仪广场D楼', '34.1251722397,108.8352441788'),
        ('东门', '34.1223789680,108.8400292397'),
        ('丁香宿舍', '34.1240798106,108.8290965557'),
        ('竹园宿舍', '34.1269218732,108.8397073746'),
        ('海棠宿舍', '34.1290800006,108.8334202766'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('EFG教学楼', '34.1240886922,108.8378190994'),
        ('信远楼', '34.1250212544,108.8389778137'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('家属区', '34.1210333687,108.8312208652'),
        ('北操场', '34.1286537082,108.8307648897'),
        ('南操场', '34.1251455952,108.8286459446'),
        ('北门', '34.1287869248,108.8375186920'),
        ('家属区与远望谷', '34.1203761044,108.8363385201'),
    ]:
    print(i[0])
"""
    Functions:
        find_path:
    Data structures:
        path_vertexs：保存遍历过的顶点，防止重复遍历
        path_length：保存遍历过的每条边的权值
"""
