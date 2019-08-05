from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Member
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
# Create your views here.
web_name='璇的購物網站'
def hello_world(request):
    return render(request, 'index.html', {
        'now': str(datetime.today()),
    })
def index(request):
    return render(request,'index.html',{'web_name':web_name})
def signup(request):
    return render(request,'signup.html',{'web_name':web_name})

def post_signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        #密碼加密
        password =  make_password(request.POST['password'])
        if Member.objects.filter(USER_ID=email).exists():
            return render(request,'signup.html',{'web_name':web_name,'signup_success':'註冊失敗，有相同帳號'})
        else:
            user=Member(USER_ID=email,USER_PASS=password,USER_NAME=username)
            user.save()
            if user:
            
                # return redirect('/',locals())
                return render(request,'index.html',{'web_name':web_name,'signup_success':'註冊成功'})
            else:
                return redirect('/signup',locals())
# def post_login(request):
#     email = request.POST['email']
#     password = request.POST['password']

#     user = authenticate(email=email,password=password)

#     if user is not None:
#         auth.login(request, user)
#         return redirect('/index',locals())
#     else: #帳密錯
#         return redirect('/index',locals())