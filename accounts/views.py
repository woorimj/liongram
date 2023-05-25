from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm, SignUpForm

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
         
