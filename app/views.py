from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView
from app.algorithm import path1 as path1, path1_end, path1_start

def make_node(location):
    return "new AMap.LngLat({}, {})".format(location.x, location.y)

class WJView(TemplateView):
    template_name = "wj.html"


class ShowView(View):
    def get(self, request):
        start = make_node(path1_start)
        end = make_node(path1_end)
        waypoints = ",".join([make_node(location) for location in path1[:-1]])
        return render(request, "show.html", context={
            "start": start,
            "end": end,
            "waypoints": waypoints
        })
