# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from appone.models import *
from django.db.models import Count

# Create your views here.


def index(request):
    return render(request, 'index.html')


'''

----Book Publisher Authors
In [29]: pubs = Publisher.objects.annotate(num_books=Count('book'))

In [30]:

In [30]: pubs
Out[30]: <QuerySet [<Publisher: Publisher object>]>

In [31]: pubs[0].num_books
Out[31]: 1


----Assets models
In [19]: print assetsNumber
<QuerySet [{'assets_type': u'server', 'dcount': 3}, {'assets_type': u'vmser', 'dcount': 2}]>



--- to do

django queryset
'''
def assets_list(request):
    assetsNumber = Assets.objects.values('assets_type').annotate(dcount=Count('assets_type'))
    return render(request, 'morris2.html', {"assetsNumber": assetsNumber})