from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

import datetime

def item(request):
    items = Item.objects.all()
    context = {'items':items} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'sellers/item_summary.html', context)# context로 html에 모든 후보에 대한 정보를 전달

def register(request):
    # if request.method == "GET":
        return render(request, 'sellers/register.html')