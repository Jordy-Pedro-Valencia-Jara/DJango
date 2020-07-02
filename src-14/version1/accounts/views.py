from django.shortcuts import render, redirect
from sjango.contrib.auth.models import User, auth
# Create your views here.
def register (request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        user=User.object.create_user(username=username,password=password
                                    email=email,first_name=first_name
                                    last_name=last_name)
        user.save();
        print('user created')
        return redirect('/')

    else:

    return render (request,'register.html')