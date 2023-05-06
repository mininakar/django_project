from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def hello(request):
    context = {'name': request.GET.get('name')}
    return render(request, 'core/hello.html', context)

def bye (request):
    context = {'name': request.GET.get('name')}
    return render(request, 'core/bye.html', context)