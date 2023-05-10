from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from .models import * 
from django.contrib.auth.decorators import login_required

def index(request):
    data2 = bogdetail.objects.all().order_by('-blogdate')[:4]
    return render(request,'index.html',{'data':data2})

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username ,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login sucessfully !!!')
            return redirect('/bloggallery/')
    return render(request,'signin.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,'logout sucessfully !!!!')
    return redirect('/')
    

def signup(request):
    if request.method=='POST':
        ud=userdetail()
        ud.username=request.POST.get('username')
        ud.useremail=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        ud.userimage=request.FILES.get('image')
 
        if User.objects.filter(username=ud.username).exists():
            messages.error(request,'username is already exists !!! ')
        elif User.objects.filter(email=ud.useremail).exists():
            messages.error(request,'useremail is already exists !!! ')
        elif password!=cpassword:
            messages.error(request,'your password and confirm password does not match !!')
        else:
            user=User.objects.create_user(username=ud.username,password=password)
            user.save()
            ud.save()
            messages.success(request,'Account is created successfully !!!!')
            return redirect('/signin/')     
    return render(request,'signup.html')

@login_required
def profile(request):
    data1=userdetail.objects.get(username=request.user.username)
    context={
        'data1':data1
    }
    return render(request,'profile.html',context)

@login_required
def addblog(request):
    if request.method != 'POST':
        return render(request,'addblog.html')
    btitle=request.POST.get('title')
    bimage=request.FILES.get('bimage')
    bdesc=request.POST.get('description')
    bdate=request.POST.get('bdate')
    bcontact=request.POST.get('contect')

    data=bogdetail(blogtitle=btitle,blogimage=bimage,blogdesc=bdesc,blogdate=bdate,blogcontact=bcontact)
    data.save()
    return redirect('/bloggallery/')

@login_required
def bloggallery(request):
    data=bogdetail.objects.all()
    return render(request,'bloggallery.html',{'data':data})


def singlepage(request,id):
    data3=bogdetail.objects.filter(id=id)
    context={
        'data':data3
     }
    return render(request,'singlepage.html',context)
    

