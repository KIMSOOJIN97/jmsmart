from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

import datetime

def item(request):
    items = Item.objects.all()
    context = {'items':items} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'sellers/item_summary.html', context)# context로 html에 모든 후보에 대한 정보를 전달

def register(request):
    if request.method == "GET":
        return render(request, 'sellers/register.html')
    elif request.method == "POST":
        name = request.POST.get('name',None)   #딕셔너리형태
        price = request.POST.get('price',None)
        description = request.POST.get('description',None)
        stock = request.POST.get('stock', None) 
        
        res_data = {} 

        if not (name and price and description and stock):
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'sellers/register.html', res_data) 
        else:
            item = Item(name= name, price=price,description=description,stock=stock)
            item.save()
        return render(request, 'sellers/success.html', res_data) 

def back(request):
    return render(request, 'sellers/item_summary.html')