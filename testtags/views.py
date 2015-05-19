# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response


def testtag(request):
    return render_to_response('testtag.html')


def testinctag(request):
    return render_to_response('book_for_title.html')
