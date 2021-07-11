from django import contrib
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.

def login_view(request): #함수이름에 view를 붙이는 이유: 그냥 login이라면 auth모듈에서 가져오는 login함수와 충돌이 나서 오류발생
  if request.method == 'POST':
    form=AuthenticationForm(request=request,data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get("username")
      password=form.cleaned_data.get("password")
      user=authenticate(request=request, username=username, password=password)
      if user is not None:
        login(request,user)

    return redirect("home")

  else:
    form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})

def logout_view(request):
  logout(request)
  return redirect("home")
  
def register_view(request):
  if request.method=='POST':
    form=RegisterForm(request.POST)
    if form.is_valid():
      user=form.save()
      login(request, user)
    return redirect('home')

  else:
    form = RegisterForm()
    return render(request,'signup.html',{'form':form})

def mypage_view(request):
    return render(request, 'mypage.html')