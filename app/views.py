#!/usr/bin/python
# coding=utf-8


from app.forms import MomentForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

def hello(name):
    name="<h1>hello</h1>"
    return HttpResponse(name)

def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app.views.hello"))
    else:
        form = MomentForm()
        args={}
        args['form']=form   
    return render_to_response('moments_input.html',args)
