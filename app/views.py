from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView
from app.algorithm import *
from app.heatmap import heatmap_js


def make_node(location):
    return "new AMap.LngLat({}, {})".format(location.x, location.y)


class WJView(TemplateView):
    template_name = "wj.html"

class IndexView(TemplateView):
    template_name = "index.html"

switch = {
    "C": pathC.result,
    "N": pathN.result,
    "S": pathS.result,
    "W": pathW.result,
    "E": pathE.result,
}


class ShowView(View):
    def get(self, request):
        path = request.GET.get("path")
        if path is None or path not in switch:
            path = "C"
        path = switch[path]

        start = make_node(path[0])
        end = make_node(path[0])
        for i in path:
            print(i.name, end="->")

        waypoints = ",".join([make_node(location) for location in path[1:-1]])
        return render(request, "show.html", context={
            "start": start,
            "end": end,
            "waypoints": waypoints,
            "path1": "->".join([i.name for i in path]),
            "path2": "->".join(reversed([i.name for i in path]))
        })


class HeatMapJsView(View):
    def get(self, request):
        return HttpResponse(heatmap_js)


class HeatMapView(TemplateView):
    template_name = "heatmap.html"
