# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
my_dict = {'insert_me':"ToKnock"}
return render(request,'index.html',context=my_dict)
