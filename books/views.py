from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from models import Book
import datetime


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})


# def current_datetime(request):
# now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('current_datetime.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def current_section(request):
    title = 'mypage'
    current_section = 'mypage->nav.html'
    return render_to_response('mypage.html', locals())


def hello(request):
    return HttpResponse("Hello world")