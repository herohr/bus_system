class Algorithm:
    @staticmethod
    def dij(locations, start):
        visited = set()
        locations.remove(start)
        path = [start]
        while len(path) != len(locations):
            start = path[-1]
            shortest_node = None
            shortest_distance = float("inf")
            for i in locations:
                if i is start or i in visited:
                    continue
                if shortest_node is None:
                    shortest_node = i
                    shortest_distance = Algorithm.get_dis(i, start)
                dis = Algorithm.get_dis(i, start)
                if dis < shortest_distance:
                    shortest_node = i
                    shortest_distance = dis
            print(path, visited, locations)
            path.append(shortest_node)
            visited.add(shortest_node)
        return path

    @staticmethod
    def get_dis(a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


_locations = [
    ('丁香宿舍', '34.1240798106,108.8290965557'),
    ('竹园宿舍', '34.1269218732,108.8397073746'),
    ('海棠宿舍', '34.1290800006,108.8334202766'),
    ('ABC教学楼', '34.1268685854,108.8310170174'),
    ('DEFG教学楼', '34.1245727376,108.8366818428'),
    ('信远楼', '34.1250212544,108.8389778137'),
    ('综合楼', '34.1281297208,108.8365101814'),
    ('家属区', '34.1210333687,108.8312208652'),
    ('北操场', '34.1286537082,108.8307648897'),
    ('南操场', '34.1250923063,108.8275408745'),
    ('北门', '34.1287869248,108.8375186920'),
    ('家属区与远望谷', '34.1203761044,108.8363385201'),
    ('图书馆', '34.1240709290,108.8330125809'),
    ('东门', '34.1223789680,108.8400292397'),
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


def generate_circle_path():
    circle_locations = [
        ('丁香宿舍', '34.1240798106,108.8290965557'),
        ('竹园宿舍', '34.1269218732,108.8397073746'),
        ('海棠宿舍', '34.1290800006,108.8334202766'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('DEFG教学楼', '34.1245727376,108.8366818428'),
        ('信远楼', '34.1250212544,108.8389778137'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('家属区', '34.1210333687,108.8312208652'),
        ('北操场', '34.1286537082,108.8307648897'),
        ('南操场', '34.1250923063,108.8275408745'),
        ('北门', '34.1287869248,108.8375186920'),
        ('家属区与远望谷', '34.1203761044,108.8363385201'),
        ('图书馆', '34.1240709290,108.8330125809'),
        ('东门', '34.1223789680,108.8400292397'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return Algorithm.dij(locations, locations[-1])


def generate_part_E():
    circle_locations = [
        ('竹园宿舍', '34.1269218732,108.8397073746'),
        ('DEFG教学楼', '34.1245727376,108.8366818428'),
        ('信远楼', '34.1250212544,108.8389778137'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('北门', '34.1287869248,108.8375186920'),
        ('家属区与远望谷', '34.1203761044,108.8363385201'),
        ('图书馆', '34.1240709290,108.8330125809'),
        ('东门', '34.1223789680,108.8400292397'),
    ]
    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return Algorithm.dij(locations, locations[-1])


def generate_part_W():
    circle_locations = [
        ('丁香宿舍', '34.1240798106,108.8290965557'),
        ('海棠宿舍', '34.1290800006,108.8334202766'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('家属区', '34.1210333687,108.8312208652'),
        ('北操场', '34.1286537082,108.8307648897'),
        ('南操场', '34.1250923063,108.8275408745'),
        ('北门', '34.1287869248,108.8375186920'),
        ('图书馆', '34.1240709290,108.8330125809'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return Algorithm.dij(locations, locations[-1])


def generate_part_N():
    circle_locations = [
        ('竹园宿舍', '34.1269218732,108.8397073746'),
        ('海棠宿舍', '34.1290800006,108.8334202766'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('DEFG教学楼', '34.1245727376,108.8366818428'),
        ('信远楼', '34.1250212544,108.8389778137'),
        ('综合楼', '34.1281297208,108.8365101814'),
        ('北操场', '34.1286537082,108.8307648897'),
        ('北门', '34.1287869248,108.8375186920'),
        ('东门', '34.1223789680,108.8400292397'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return Algorithm.dij(locations, locations[-1])


def generate_part_S():
    circle_locations = [
        ('丁香宿舍', '34.1240798106,108.8290965557'),
        ('ABC教学楼', '34.1268685854,108.8310170174'),
        ('DEFG教学楼', '34.1245727376,108.8366818428'),
        ('家属区', '34.1210333687,108.8312208652'),
        ('南操场', '34.1250923063,108.8275408745'),
        ('北门', '34.1287869248,108.8375186920'),
        ('家属区与远望谷', '34.1203761044,108.8363385201'),
        ('图书馆', '34.1240709290,108.8330125809'),
        ('东门', '34.1223789680,108.8400292397'),
    ]

    locations = []
    for name, l in circle_locations:
        x, y = l.split(",")
        locations.append(Location(name, float(y), float(x)))
    return Algorithm.dij(locations, locations[-1])


# print(locations)

path1_start = Location.from_str('东门', '34.1223789680,108.8400292397')
path1_end = Location.from_str('东门', '34.1223789680,108.8400292397')
path1 = generate_circle_path()  # 外环线

pathE_start = path1_start
pathE_end = path1_end
pathE = generate_part_E()
