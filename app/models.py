from django.db.models import *


# Create your models here.


class WJ(Model):
    id = AutoField(primary_key=True)
    q1 = BooleanField(default=True, verbose_name="是否需要公共交通")
    q2 = CharField(max_length=8, verbose_name="交通方式",
                   choices=(("minibus", "小型公交车"), ("ecar", "电瓶车"), ("railway", "轨道交通")))
    q3 = CharField(max_length=32, verbose_name="现在在何处")
    q4 = CharField(max_length=32, verbose_name="去往何处")
    q5 = TextField(verbose_name="最希望开通的路线")

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.q1, self.q2, self.q3, self.q4, self.q5)


class Site(Model):
    name = CharField(max_length=32, primary_key=True)
    location = TextField(default="")


class Station(Model):
    id = AutoField(primary_key=True)
    site = ForeignKey(Site, on_delete=CASCADE)
    waiting = PositiveIntegerField(verbose_name="正在等待的人数", default=0)


class Route(Model):
    id = AutoField(primary_key=True)
    stations = ManyToManyField(Station)


class Bus(Model):
    id = AutoField(primary_key=True)
    payload = PositiveIntegerField(verbose_name="车上人数", default=0)

    route = ForeignKey(Route, on_delete=CASCADE)
    station = ForeignKey(Station, on_delete=CASCADE)


site_names = ['丁香宿舍', '竹园宿舍', '海棠宿舍', '丁香食堂', '竹园食堂', '海棠食堂', 'A教学楼', 'B教学楼', 'C教学楼',
              'D教学楼', 'E教学楼', 'F教学楼', 'G教学楼', '信远楼', '工训中心', '新综', '老综', '行政楼', '家属区',
              '北操场', '南操场', '大学生活动中心', "北门", "东门", "图书馆"]


def site_init():
    for i in site_names:
        s, _ = Site.objects.get_or_create(name=i)
        s.save()


# site_init()


def create_wj(q1, q2, q3, q4, q5, q6):
    a = WJ(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6)
    a.save()
#
#
# _locations = [
#     ('丁香宿舍', '34.1207047372,108.8284850121'),
#     ('竹园宿舍', '34.1269218732,108.8397073746'),
#     ('海棠宿舍', '34.1292842650,108.8344931602'),
#     ('ABC教学楼', '34.1268685854,108.8310170174'),
#     ('D教学楼', '34.1248969134,108.8350939751'),
#     ('EFG教学楼', '34.1238844153,108.8372182846'),
#     ('信远楼', '34.1250212544,108.8389778137'),
#     ('工训中心', '34.1263889937,108.8382267952'),
#     ('综合楼', '34.1281297208,108.8365101814'),
#     ('行政楼', '34.1221436007,108.8383340836'),
#     ('家属区', '34.1208823760,108.8289141655'),
#     ('北操场', '34.1301190794,108.8307595253'),
#     ('南操场', '34.1250923063,108.8275408745'),
#     ('北门', '34.1287869248,108.8375186920'),
#     ('东门', '34.1219126737,108.8403725624'),
#     ('E区家属区与远望谷', '34.1203761044,108.8363385201'),
#     ('图书馆', '34.1239865538,108.8333237171'),
# ]
#
#
# class Location:
#     def __init__(self, name, x, y):
#         self.name = name
#         self.x = x
#         self.y = y
#
#
# locations = [Location for name, l in _locations]
