# -*- coding: utf-8 -*-

from django import template
from books.models import Book

register = template.Library()


@register.inclusion_tag('book_for_title.html')
def books_for_author(author):
    books = Book.objects.filter(authors__id=author.id)
    return {'books': books}