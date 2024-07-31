from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as user_login ,logout as user_logout

# Create your views here.
def Userlogin(req):
    user = None
    if req.method == 'POST' :
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req,username = username, password = password)
        if user is not None:
            if user.is_active:
                user_login(req,user)
                return redirect('Home')
    return render(req,'Login.html',{'user':user})

def Userlogout(req):
    user_logout(req)
    return redirect('Home')

def Signup(req):
    userdata = None
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        password = req.POST.get('password')
        repassword = req.POST.get('repassword')
        if password == repassword:
            userdata = User.objects.create_user(first_name=name,email=email,username=email,password=password)
            userdata.save()
            return redirect('Home')
    return render(req,'SignUp.html',{'user' :userdata})