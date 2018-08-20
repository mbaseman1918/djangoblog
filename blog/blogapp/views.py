from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import BlogPost, Comment
# Create your views here.

def index(request):
    blogpost_list = BlogPost.objects.all()
    comment_list = Comment.objects.all()
    context = {
    'blogposts':blogpost_list,
    'comments':comment_list,
    }
    return render(request, 'blogapp/index.html', context)

def add_blogpost(request):
    if request.method == "POST":
        new_user = request.user.username
        new_title = request.POST['title']
        new_body = request.POST['body']
        new_blogpost = BlogPost(user=new_user, title=new_title, body=new_body)
        new_blogpost.save()
    return HttpResponseRedirect(reverse('blogapp:index'))

def delete_blogpost(request, pk):
    target_blogpost = get_object_or_404(Blogpost, pk=pk)
    target_blogpost.delete()
    return HttpResponseRedirect(reverse('blogapp:index'))

def add_comment(request, pk):
    if request.method == "POST":
        new_user = request.user.username
        new_blogpost = BlogPost.objects.filter(pk=pk)[0]
        new_body = request.POST['body']
        new_comment = Comment(user=new_user, blogpost=new_blogpost, body=new_body)
        new_comment.save()
    return HttpResponseRedirect(reverse('blogapp:index'))

def delete_comment(request, pk):
    target_comment = get_object_or_404(Comment, pk=pk)
    target_comment.delete()
    return HttpResponseRedirect(reverse('blogapp:index'))
