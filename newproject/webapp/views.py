from django.shortcuts import render

from django.template import loader

from django.http import HttpResponse


def hellow(request):
    template = loader.get_template('hellow.html')
    name  = {
        'emp':'madhu'

    }
    return HttpResponse(template.render(name))
