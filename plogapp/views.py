from django.shortcuts import render , get_object_or_404
from .models import post
# Create your views here.

def postList(request):
    posts = post.objects.all()
    return render(request,"home.html",{"posts": posts})

def post_details(request,pk):
    postd = get_object_or_404(post,pk=pk)
    return render(request , "post_detail.html",{"postd":postd})