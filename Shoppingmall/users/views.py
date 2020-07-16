from django.shortcuts import render,redirect
from users.models import User
from django.contrib import auth

from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password 
from django.contrib import messages



def home(request):
<<<<<<< HEAD
    return render(request, 'users/home.html')
=======
    user_id = request.session.get('user')
    if user_id :
        myuser_info = User.objects.get(pk=user_id)
#        return HttpResponse(myuser_info.userID)
        
    return render(request, 'home.html')
>>>>>>> master

def signup(request):
    return render(request, 'signup.html')

def users_signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
<<<<<<< HEAD
        return render(request, 'users/signup.html')
=======
        return render(request, 'users_signup.html')
>>>>>>> master

    elif request.method == "POST":
        ID = request.POST.get('ID',None)   #딕셔너리형태
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        username = request.POST.get('username', None)   #딕셔너리형태
        postcode = request.POST.get('postcode', None)
        address = request.POST.get('address1', None)+request.POST.get('address2', None)
        number = request.POST.get('number',None)
        e_mail = request.POST.get('e_mail',None)

        if not (ID and username and password and re_password and address and number and e_mail and postcode) :
<<<<<<< HEAD
            res_data['error'] = "모든 값을 입력해야 합니다."
            print("here1")
            return render(request, 'users/signup.html', res_data) #register를 요청받으면 register.html 로 응답.

        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
            print("gere2")
            return render(request, 'users/signup.html', res_data) #register를 요청받으면 register.html 로 응답.
        else :
            user = User(userID = ID, password=make_password(password),username=username,postcode = postcode, address = address, phone=number,e_mail = e_mail)
            user.save()
        return render(request, 'users/home.html', res_data) #register를 요청받으면 register.html 로 응답.
=======
            messages.add_message(request, messages.INFO, '모든 값을 입력해야 합니다.') # 첫번째, 초기지원
            return render(request, 'users_signup.html') #register를 요청받으면 register.html 로 응답.

        if password != re_password :
            #return HttpResponse('비밀번호가 다릅니다.')
            messages.add_message(request, messages.INFO, '비밀번호가 다릅니다.') # 첫번째, 초기지원
            return render(request, 'users_signup.html') #register를 요청받으면 register.html 로 응답.       

        else :
            user = User(userID = ID, password=make_password(password),username=username,postcode = postcode, address = address, phone=number,e_mail = e_mail)
            user.save()            
            return redirect('/')
>>>>>>> master

            #return render(request, 'home.html', res_data) #register를 요청받으면 register.html 로 응답.


def login(request):
    if request.method == "GET" :
        return render(request, 'users/login.html')

    elif request.method == "POST":
        login_username = request.POST.get('ID', None)
        login_password = request.POST.get('password', None)


        if not (login_username and login_password):
            messages.add_message(request, messages.INFO, '아이디와 비밀번호를 모두 입력하세요.') # 첫번째, 초기지원
        else : 
<<<<<<< HEAD
            myuser = User.objects.get(userID=login_username) 
            print(login_username)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.password):
                request.session['user'] = myuser.id
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'users/login.html',response_data)
=======
            try:
                myuser = User.objects.get(userID=login_username) 
                print(myuser)
                print("1")
                #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
                if check_password(login_password, myuser.password):
                    request.session['user'] = myuser.id 
                    #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    #세션 user라는 key에 방금 로그인한 id를 저장한것.
                    return redirect('/')
                else:
                    messages.add_message(request, messages.INFO, '비밀번호가 틀렸습니다.') # 첫번째, 초기지원
            #아이디가 존재하지 않을 경우
            except User.DoesNotExist:
                messages.add_message(request, messages.INFO, '가입하지 않은 아이디입니다.') # 첫번째, 초기지원

        return render(request, 'login.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
>>>>>>> master
