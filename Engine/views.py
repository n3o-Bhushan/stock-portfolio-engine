# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def my_view(request):
    # View code here...
     return render(request, 'index.html',{})
   





