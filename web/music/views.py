from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from .models import Member,board
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import auth  # 別忘了import auth
from django.forms import Form, fields
from django.core import serializers
# import PublicFun
# Create your views here.
# web_name='璇的購物網站'
def hello_world(request):
    return render(request, 'index.html', {
        'now': str(datetime.today()),
    })
def index(request):
    title=board.objects.filter(USER_ID='roger')
    dic={}
    dic["USER_ID"]=title[0].USER_ID
    dic["USER_TITLE"]=title[0].USER_TITLE
    dic["USER_CONTENT"]=title[0].USER_CONTENT
    dic["OP_DATE"]=title[0].OP_DATE
    # print(dic)
  
    return render(request,'index.html',{'title': json.dumps(dic,cls=DjangoJSONEncoder)})
def signup(request):
    return render(request,'signup.html')
    # return redirect('/signup',locals)
def login(request):
    return render(request,'login.html')

#註冊
def post_signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST': 
        message='檢查輸入內容'
        username = request.POST['username']

        email = request.POST['email']
        #密碼加密
        password = request.POST['password']
        # #CheckUser
        # if PublicFun.CheckUser(username,password,email) !="":
        #     message=PublicFun.CheckUser(username,password,email)
        #     return render(request,'signup.html',{'web_name':web_name,'message':message})

        password = make_password(password)
        
        if Member.objects.filter(USER_ID=email).exists():
            message='已有相同帳號!'
            return render(request,'signup.html',{'message':message})
        else:
            user=Member(USER_ID=email,USER_PASS=password,USER_NAME=username)
            user.save()
            if user:
            
                #  return redirect('/login',{'signup_success':'註冊成功'})
                 return render(request,'login.html',{'signup_success':'註冊成功'})
                # return render(request,'/',{'web_name':web_name,'signup_success':'註冊成功'})
            else:
                return redirect('/signup',locals())
#登入
def post_login(request):
    email = request.POST['email']
    password = request.POST['password']
    dicERR={}
    dicERR['USER_EMAIL']=email
    dicERR['USER_PASS']=password
    
    # user= auth.authenticate(username=email,password=password)
    if Member.objects.filter(USER_ID=email).exists():
        user=Member.objects.filter(USER_ID=email)
        if check_password(password ,user[0].USER_PASS) :
            request.session['USER']={'USER_NAME':user[0].USER_NAME,'CREATE_DATE':str(user[0].CREATE_DATE)[:10]}
            # redirect(index)
            # return render(request,'index.html')
            return redirect('/')
        else:
            return render(request,'login.html',{'message':'密碼錯誤','dicERR':dicERR})
        # return render(request,'login.html',{'user':user[0].USER_NAME})
    else:
        return render(request,'login.html',{'message':'無此帳號','dicERR':dicERR})
    # user = authenticate(email=email,password=password)


#登出
def logout(request):
    del request.session['USER']
    return redirect('/')
#取得文章API
def GetArticleAPI(request):
    article=board.objects.all()
    data = serializers.serialize('json',article)
    return JsonResponse({'data':data})