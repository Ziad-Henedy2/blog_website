# this is function based view 

''' 
from django.shortcuts import render , get_object_or_404
from .models import post

def postList(request):
    posts = post.objects.all()
    return render(request,"home.html",{"posts": posts})

def post_details(request,pk):
    postd = get_object_or_404(post,pk=pk)
    return render(request , "post_detail.html",{"postd":postd})
'''
# now we will switch the code to generic class based from .views import 

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView , UpdateView ,DeleteView
from django.urls import reverse_lazy
from .models import post

class postListView(ListView):
    model =post
    template_name = "home.html"

class detailPostView(DetailView):
    model=post
    template_name = "post_detail.html"

class postCreateView(CreateView):
    model = post
    template_name = "new_post.html"
    fields = ["title","author","body"]

class postupdate(UpdateView):
    model = post
    template_name = "post_update.html"
    fields = ["title","body"]

class deletePost(DeleteView):
    model = post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


