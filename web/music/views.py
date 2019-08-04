from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from models import Member
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
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user=Member(USER_ID=email,USER_PASS=password,USER_NAME=username)
    user.save()
    if user:
        return redirect('/',locals())
    else:
        return redirect('/signup',locals())