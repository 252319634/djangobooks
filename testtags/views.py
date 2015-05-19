# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response


def cut_blank(request):
    return render_to_response('cut_blank.html', {'teststr': '1 2 3 4 5 6 7'})
