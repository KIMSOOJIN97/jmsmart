from django.shortcuts import render, redirect
from users.models import *
from sellers.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.utils import timezone


def home(request):
    request.session.get('user')
    products = Item.objects.all().order_by('-view')
    allcategory = Category.objects.all()
    # 모든 item을 product_list에 저장
    list = {'products': products}
    list['allcategory'] = allcategory

    return render(request, 'users/home.html', list)


def signup(request):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}
    return render(request, 'users/signup.html', list)


def users_signup(request):  # 회원가입 페이지를 보여주기 위한 함수
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}
    if request.method == "GET":
        return render(request, 'users/users_signup.html', list)

    elif request.method == "POST":
        ID = request.POST.get('ID', None)  # 딕셔너리형태
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        username = request.POST.get('username', None)  # 딕셔너리형태
        postcode = request.POST.get('postcode', None)
        address = request.POST.get('address1', None)
        detail_address = request.POST.get('address2', None)
        number = request.POST.get('number', None)
        e_mail = request.POST.get('e_mail', None)

        if not (ID and username and password and re_password and address and number and e_mail and postcode):
            messages.add_message(request, messages.INFO,
                                 '모든 값을 입력해야 합니다.')  # 첫번째, 초기지원
            # register를 요청받으면 register.html 로 응답.
            return render(request, 'users/signup.html', list)

        if password != re_password:
            # return HttpResponse('비밀번호가 다릅니다.')
            messages.add_message(request, messages.INFO,
                                 '비밀번호가 다릅니다.')  # 첫번째, 초기지원
            # register를 요청받으면 register.html 로 응답.
            return render(request, 'users_signup.html', list)

        else:
            user = User(userID=ID, password=make_password(password), username=username, postcode=postcode,
                        address=address, detail_address=detail_address, phone=number, e_mail=e_mail)
            user.save()
            return redirect('/')

            # return render(request, 'home.html', res_data) #register를 요청받으면 register.html 로 응답.


def login(request):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    if request.method == "GET":
        return render(request, 'users/login.html', list)

    elif request.method == "POST":
        login_username = request.POST.get('ID', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            messages.add_message(request, messages.INFO,
                                 '아이디와 비밀번호를 모두 입력하세요.')  # 첫번째, 초기지원
        else:
            try:
                myuser = User.objects.get(userID=login_username)
                # db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
                if check_password(login_password, myuser.password):
                    request.session['user'] = myuser.userID
                    # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                    return redirect('/')
                else:
                    messages.add_message(
                        request, messages.INFO, '비밀번호가 틀렸습니다.')  # 첫번째, 초기지원
            # 아이디가 존재하지 않을 경우
            except User.DoesNotExist:
                messages.add_message(request, messages.INFO,
                                     '가입하지 않은 아이디입니다.')  # 첫번째, 초기지원

        return render(request, 'users/login.html', list)


def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('/')


def mypage(request):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}
    myuser_id = request.session.get('user')
    myuser_info = User.objects.get(userID=myuser_id)
    list['myuser_info'] = myuser_info
    return render(request, 'users/mypage.html', list)


def notice(request):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}
    notice_list = Notice.objects.all()
    list['notice_list'] = notice_list
    return render(request, 'users/notice.html', list)


def noticedetail(request, pk):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    notice = Notice.objects.get(id=pk)
    list['notice'] = notice

    return render(request, 'users/notice_detail.html', list)


def category(request, category):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    # category 테이블에서 해당 카테고리에 관한 값을 받아온다
    try:
        cate = Category.objects.get(name=category)

        sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

        #  products = Item.objects.filter(category = category)
        # 모든 item을 product_list에 저장
        # cate.id를 통해 foreign key 조회 가능
        if sort == 'view':
            products = Item.objects.filter(category=cate.id).order_by('-view')
        elif sort == 'low_price':
            products = Item.objects.filter(
                category=cate.id).order_by('price')  # 오름차순
        elif sort == 'high_price':
            products = Item.objects.filter(
                category=cate.id).order_by('-price')  # 내림차순
        else:
            products = Item.objects.filter(
                category=cate.id).order_by('-upload_date')
        list['products'] = products

        return render(request, 'users/category.html', list)

    except Category.DoesNotExist:
        list['products'] = None
        return render(request, 'users/category.html', list)


def product(request, category, product):

    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}
    thisproduct = Item.objects.get(name=product)
    thisproduct.view = thisproduct.view + 1
    thisproduct.save()
    list['product'] = thisproduct

    # list['product3'] = thisproduct
    list['product2'] = product
    list['category'] = category

    if request.method == "GET":
        cart = request.GET.get('cart')
        if (cart):
            myuser_id = request.session.get('user')

            item_count = request.GET.get('item_count')
            item = thisproduct
            user = User.objects.get(userID=myuser_id)

            addcart = Cart(user=user, item=item, item_count=item_count)
            addcart.save()
            info = {}
            info['confirm'] = "ok"
            return JsonResponse(info)
        else:
            return render(request, 'users/product.html', list)

    return render(request, 'users/product.html', list)

#개인 장바구니
def cart(request, userid):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    user = User.objects.get(userID=userid)
    cartitem = Cart.objects.filter(user=user)
    list['cart'] = cartitem

    return render(request, "users/cart.html", list)

@csrf_exempt
def cart_delete(request, userid):
    print('cart_delete')
    checkArr = request.POST.get('ch_box')
    checklist = checkArr.split(',')
    print(len(checklist))
    for i in checklist:
        cartitem = Cart.objects.get(id=int(i))
        cartitem.delete()
        print('delete ok')
    info = {}
    info['confirm'] = "ok"
    return JsonResponse(info)
    # return render(request, "users/cart.html", list)

#개인 주문/배송현황
def ordering(request,userid):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    user = User.objects.get(userID=userid)
    ordering = Buy.objects.filter(user=user,orderstate='주문완료' )
    list['ordering']=ordering
    #!!!!!!!!!!!!!!!!!!!!!!!!!배송완료가아닐때로 고쳐야함. orderstate=!'배송완료'



    return render(request, 'users/ordering.html', list)


#개인 구매목록
def buylist(request,userid):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    user = User.objects.get(userID=userid)
    buy = Buy.objects.filter(user=user)
    list['buylist'] = buy
    # 나중에 구매한꺼번에 한것대로 꼭 묶어서보여주기!!
    # buydatelist=buy.objects.values_list('buy_date')
    # buydatelist[0].strftime('%Y-%m-%d %H')
    # print(buydatelist)
    # set(buydatelist)
    # print(buydatelist)

    return render(request, 'users/buylist.html', list)

@csrf_exempt
def buylist_delete(request, userid):
    print('buylist_delete')
    checkArr = request.POST.get('ch_box')
    print(checkArr)
    checklist = checkArr.split(',')
    print(len(checklist))
    for i in checklist:
        buyitem = Buy.objects.get(id=int(i))
        buyitem.delete()
        print('delete ok')
    info = {}
    info['confirm'] = "ok"
    return JsonResponse(info)



# 장바구니에서 -->구매 : 사용자의 카트목록 중 선택된 것만 불러오기
@csrf_exempt
def order_form(request, userid):
    print('order form')
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    user = User.objects.get(userID=userid)
    list['user'] = user
    if request.method == "GET":
        print('get')
        checkArr = request.GET.get('ch_box')
        print(checkArr)
        if (checkArr):#check된게있으면
            if ( ',' in checkArr): #다중선택이라면
                checklist = checkArr.split(',')
                checklen=len(checklist)
                for i in range( checklen):
                    #?????????????????????다중선택하면왜안되지????????? OverflowError뜸 , 장바구니에 여러개잇으면???
                    print('hihi')
                    print(i)
                    cartitem = Cart.objects.get(id=int(checklist[i]))
                    print(checklist[i])
                    print('c')
                    total = int(cartitem.item_count)*int(cartitem.item.price)
                    print('b')
                    buy = Buy(user=user, item=cartitem.item, item_count=cartitem.item_count, postcode=user.postcode,
                              address='0', detail_address='0', phone='0', price=total)
                    print('a')
                    buy.save()
                    cartitem.delete()
            else: #단일 선택이 됬다면
                cartitem = Cart.objects.get(id=int(checkArr))
                total = int(cartitem.item_count)*int(cartitem.item.price)
                buy = Buy(user=user, item=cartitem.item, item_count=cartitem.item_count, postcode=user.postcode,
                          address=user.address, detail_address=user.detail_address, phone=user.phone, price=total)
                buy.save()
                checklen=1
                cartitem.delete()

            info={}
            info['confirm'] = "ok"
            request.session['checklen'] = checklen

            return JsonResponse(info)

        else:#None이면
            print('else문 None일때')
            checklen=request.session.get('checklen')
            buy = Buy.objects.filter(user=user)
            buylist = buy[:checklen]
            list['buylist']=buylist
            print(buylist)

            del(request.session['checklen'] )
            return render(request, 'users/order_form.html', list)


    elif request.method=="POST":
        print('post')
        checkArr = request.POST.get('ch_box')
        print(checkArr)


        # #사실버튼누르면으로 바꿔야함..
        # buy = Buy(user=user, item=cartitem.item, item_count=cartitem.item_count, postcode=user.postcode,
        #           address=user.address, detail_address=user.detail_address, phone=user.phone, price=total)
        # buy.save()

    # product = Item.objects.get(name=product)
    # total = product.price * int(quantity)
    #
    # list['product'] = product
    #
    # list['quantity'] = quantity
    #
    # buy = Buy(user=user, item=product, item_count=quantity, postcode=user.postcode,
    #           address=user.address, detail_address=user.detail_address, phone=user.phone, price=total)
    # buy.save()

        return render(request, 'users/order_form.html', list)

# 상세상품페이지 --> 구매하기 : 해당상품만 구매
def only_order_form(request, category, product, quantity):
    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    myuser_id = request.session.get('user')
    user = User.objects.get(userID=myuser_id)
    list['user'] = user

    product = Item.objects.get(name=product)
    print(quantity)
    total = product.price * int(quantity)

    list['product'] = product
    list['quantity'] = quantity

    buy = Buy(user=user, item=product, item_count=quantity, postcode=user.postcode,
              address=user.address, detail_address=user.detail_address, phone=user.phone, price=total)
    buy.save()

    return render(request, 'users/only_order_form.html', list)

# 실제결제하기
def purchase(request):
    ID = request.GET.get('username')

    allcategory = Category.objects.all()
    list = {'allcategory': allcategory}

    myuser_id = request.session.get('user')
    user = User.objects.get(userID=myuser_id)
    list['user'] = user

    return render(request, 'users/purchase_list.html', list)

