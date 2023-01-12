from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    a = Post.objects.all()
    lis = []
    for i in a:
        lis.append(i)
    return render(request,'home.html',{"datas":lis})
    
def hello(request):
    return render(request,'hello.html')