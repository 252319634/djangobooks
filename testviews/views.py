__author__ = 'Administrator'
from django.shortcuts import render_to_response
from django.template import RequestContext


def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }


def view_1(request, n):
    # ...
    return render_to_response('template1.html',
                              {'message': 'I am view 1.'},
                              context_instance=RequestContext(request, processors=[custom_proc]))


def view_2(request):
    # ...
    return render_to_response('template2.html',
                              {'message': 'I am the second view.'},
                              context_instance=RequestContext(request, processors=[custom_proc]))


def view(request, n):
    if n == '1':
        return render_to_response('template1.html',
                                  {'message': 'I am view 1.'},
                                  context_instance=RequestContext(request, processors=[custom_proc]))
    if n == '2':
        return render_to_response('template2.html',
                                  {'message': 'I am the second view.'},
                                  context_instance=RequestContext(request, processors=[custom_proc]))