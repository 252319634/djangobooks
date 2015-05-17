# coding:utf8
from django.db import models


class Publisher(models.Model):
    city_in_choices = (('LinFen', '临汾'),)

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60, choices=city_in_choices, default='unknown')
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title