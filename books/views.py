# coding: utf8
from django.core.mail import send_mail
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from models import Book
import datetime

# def search_form(request):
# return render_to_response('search_form.html')


def showbook(request):
    return render_to_response('result_snippet.html', {'title': 'title123', 'author': '麦'})


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search.html',
                                      {'books': books, 'query': q})
    return render_to_response('search.html', {'errors': errors})


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
    book_list = Book.objects.order_by('-publication_date')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})


# def current_datetime(request):
# now = datetime.datetime.now()
# html = "<html><body>It is now %s.</body></html>" % now
# return HttpResponse(html)
# def current_datetime(request):
# now = datetime.datetime.now()
# t = get_template('current_datetime.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def current_section(request):
    a = request.REQUEST.get('a', '0')
    title = 'mypage'
    current_section = 'mypage->nav.html'
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    # return HttpResponse("Your browser is %s" % ua)
    return render_to_response('mypage.html', locals())


# def display_meta(request):
# values = request.META.items()
#     values.sort()
#     html = []
#     for k, v in values:
#         if str(v).startswith('<'):
#              v = '&lt;'+str(v)[1:-1]+'&gt;'
#         html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#     return HttpResponse('<table>%s</table>' % '\n'.join(html))

def display_meta(request):
    re = request.META.items()
    re.sort()
    s = '<table>'
    for k, v in re:
        v = str(v).replace('<', '&lt;').replace('<', '&gt;')
        s += ('<tr><td>%s</td><td>%s</td></tr>\n' % (k, v))
    s += '</table>'
    return HttpResponse(s)


def hello(request):
    return HttpResponse("Hello world")