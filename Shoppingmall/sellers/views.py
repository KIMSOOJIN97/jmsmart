# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from django.utils import  timezone

from django.contrib import auth

from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.views.generic import *



def signup(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'seller_signup.html')

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
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'seller_signup.html', res_data) #register를 요청받으면 register.html 로 응답.

        if password != re_password :
            #return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'seller_signup.html', res_data) #register를 요청받으면 register.html 로 응답.
        else :
            seller = Seller(sellerID = ID, password=make_password(password),company_name=company_name,postcode = postcode, address = address, phone=number,e_mail = e_mail,corporate_number= corporate_number )
            seller.save()
            return redirect('/')


from django.views import generic

class NoticeListView(generic.ListView):
    model = Notice
    paginate_by = 10

class NoticeDetailView(generic.DetailView):
    model = Notice

def notice(request):
    notice_list = Notice.objects.all()
    return render(request,'notice.html',{'notice_list':notice_list})

def noticedetail(request):
    notice_list = Notice.objects.all()
    return render(request,'notice_detail.html',{'notice_list':notice_list})

def notice_addPost(request):
    if request.method == "GET":
        return render(request, 'sellers/notice_addPost.html')

    elif request.method == "POST":
        title = request.POST.get('TITLE',None)
        content =request.POST.get('CONTENTS',None)

        res_data = {}
        if not (title and content) :
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'sellers/notice_addPost.html', res_data) #register를 요청받으면 register.html 로 응답.

        else :
            # author = "ddd",
            addPost = Notice(title=title,content=content)
            addPost.save()
            return redirect('/sellers/notice/')

