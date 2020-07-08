from django.shortcuts import render,redirect
from users.models import User
from django.contrib import auth

from django.http import HttpResponse
from django.contrib.auth.hashers import make_password



def home(request):
    return render(request, 'home.html')

def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        print("here")
        return render(request, 'signup.html')

    elif request.method == "POST":
        print("here2")
        ID = request.POST.get('ID',None)   #딕셔너리형태
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        username = request.POST.get('username', None)   #딕셔너리형태
        postcode = request.POST.get('postcode', None)
        address = request.POST.get('address1', None)+request.POST.get('address2', None)
        number = request.POST.get('number',None)
        e_mail = request.POST.get('e_mail',None)
        print(address)

        print(address)
        res_data = {} 
        if not (ID and username and password and re_password and address and number and e_mail and postcode) :
            res_data['error'] = "모든 값을 입력해야 합니다."
            print("hello3")
            return render(request, 'signup.html', res_data) #register를 요청받으면 register.html 로 응답.


        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
            print("hello2")
            return render(request, 'signup.html', res_data) #register를 요청받으면 register.html 로 응답.


        else :
            user = User(userID = ID ,  password=make_password(password),username=username,postcode = postcode, address = address, phone=number,e_mail = e_mail)
            user.save()
            print("hello1")
        return render(request, 'home.html', res_data) #register를 요청받으면 register.html 로 응답.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            return render(request , 'login.html',{'error' : 'username or password is incorrect'})
    else:
        return render(request,'login.html')