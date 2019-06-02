from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class WJView(TemplateView):
    template_name = "wj.html"