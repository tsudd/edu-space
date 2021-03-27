from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(req):
    template = loader.get_template("eduspace/index.html")
    contex = {}
    return HttpResponse(template.render(contex, req))
