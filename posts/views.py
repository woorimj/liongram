from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import Post

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

@login_required
def post_create_view(request):
    if request.method == "GET":
        return render(request, 'posts/post_form.html')
    else: ## 글을 입력받으면 POST
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user
        )
        return redirect('index')

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

# Create your views here.
# FBV -> 함수기반 view
def url_view(request):
    print('url_view()')
    data = {'code': '001', 'msg':'OK'}
    return HttpResponse('<h1>url_view</h1>')
    #return JsonResponse(data)

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

# CBV -> class기반 
class class_view(ListView):
    model = Post
    #ordering = ['-id']
    template_name = 'cbv_view.html'

def function_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list': object_list})