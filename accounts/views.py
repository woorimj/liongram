from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import UserCreateForm, SignUpForm

from users.models import User

def signup_view(request):
    #GET요청시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    else:
        #POST 요청시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)

        if form.is_valid():
            #회원가입처리
            instance = form.save()
            return redirect('index')
            #username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            #password2 = form.cleaned_data['password2']
        else:
            #redirect
            return redirect('accounts:signup')
        
def login_view(request):
    if request.method == 'GET':
       return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            #로그인 처리
            login(request, form.user_cache)
            return redirect('index')
        else:
            #로그인 실패
            return render(request, 'accounts/login.html', {'form':form})
         
#        username = request.POST.get('username')
#       if username == "" or username == None:
#          pass
#     user = User.objects.get(username==username)
#    if user == None:
#       pass
 # password = request.POST.get('password')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
       