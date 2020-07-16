from django.shortcuts import render
<<<<<<< HEAD
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
=======

# Create your views here.
from django.shortcuts import render,redirect
from sellers.models import Seller
from django.contrib import auth

from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password 

from django.contrib import messages


def home(request):
#        return HttpResponse( .userID)     
    return render(request, 'sellers/home.html')

def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'sellers/signup.html')

    elif request.method == "POST":
        ID = request.POST.get('ID',None)   #딕셔너리형태
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        company_name = request.POST.get('companyname', None)   #딕셔너리형태
        postcode = request.POST.get('postcode', None)
        address = request.POST.get('address1', None)+request.POST.get('address2', None)
        number = request.POST.get('number',None)
        e_mail = request.POST.get('e_mail',None)
        corporate_number = request.POST.get('corporate_number',None)

        res_data = {} 
        if not (ID and company_name and password and re_password and address and number and e_mail and postcode and corporate_number) :
            messages.add_message(request, messages.INFO, '모든 값을 입력해야 합니다.') # 첫번째, 초기지원
            return render(request, 'sellers/signup.html', res_data) #register를 요청받으면 register.html 로 응답.

        if password != re_password :
            messages.add_message(request, messages.INFO, '비밀번호가 다릅니다.') # 첫번째, 초기지원
            return render(request, 'sellers/signup.html', res_data) #register를 요청받으면 register.html 로 응답.
        else :
            seller = Seller(sellerID = ID, password=make_password(password),company_name=company_name,postcode = postcode, address = address, phone=number,e_mail = e_mail,corporate_number= corporate_number )
            seller.save()
            return redirect('/')


def login(request):
    response_data = {}
    if request.method == "GET" :
        return render(request, 'sellers/login.html')

    elif request.method == "POST":
        login_username = request.POST.get('ID', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 모두 입력해주세요.') # 첫번째, 초기지원
        else : 
            try:
                myuser = Seller.objects.get(sellerID=login_username) 
                #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
                if check_password(login_password, myuser.password):
                    request.session['seller'] = myuser.id 
                    #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    #세션 user라는 key에 방금 로그인한 id를 저장한것.
                    return redirect('/sellers')
                else:
                    messages.add_message(request, messages.INFO, '비밀번호가 틀렸습니다.') # 첫번째, 초기지원

            except Seller.DoesNotExist:
                messages.add_message(request, messages.INFO, '가입하지 않은 아이디입니다.') # 첫번째, 초기지원

        return render(request, 'sellers/login.html',response_data)

def logout(request):
    if request.session.get('seller'):
        del(request.session['seller'])
    return redirect('/')
>>>>>>> master
