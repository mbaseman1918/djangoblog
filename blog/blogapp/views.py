from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.urls import reverse
from .models import BlogPost, Comment
# Create your views here.

def index(request):
    blogpost_list = BlogPost.objects.all()
    for blogpost_item in blogpost_list:
        blogpost_item.comments = Comment.objects.filter(blogpost=blogpost_item)
    if User.is_authenticated:
        context = {
        'user':request.user,
        'blogposts':blogpost_list,
        }

    return render(request, 'blogapp/index.html', context)

@permission_required('blogapp.add_blogpost')
def add_blogpost(request):
    if request.method == "POST":
        new_user = request.user
        new_title = request.POST['title']
        new_body = request.POST['body']
        new_blogpost = BlogPost(user=new_user, title=new_title, body=new_body)
        new_blogpost.save()
    return HttpResponseRedirect(reverse('blogapp:index'))

def delete_bp_check(request, pk):
    target_blogpost = get_object_or_404(BlogPost, pk=pk)
    return target_blogpost.user == request.user

def delete_blogpost(request, pk):
    if delete_bp_check(request, pk):
        target_blogpost = get_object_or_404(BlogPost, pk=pk)
        target_blogpost.delete()
        return HttpResponseRedirect(reverse('blogapp:index'))
    else:
        return HttpResponseRedirect(reverse('blogapp:index'))

@permission_required('blogapp.add_comment')
def add_comment(request, pk):
    if request.method == "POST":
        new_user = request.user
        new_blogpost = BlogPost.objects.filter(pk=pk)[0]
        new_body = request.POST['body']
        new_comment = Comment(user=new_user, blogpost=new_blogpost, body=new_body)
        new_comment.save()
    return HttpResponseRedirect(reverse('blogapp:index'))

def delete_comment_check(request, pk):
    target_comment = get_object_or_404(Comment, pk=pk)
    return target_comment.user == request.user


def delete_comment(request, pk):
    if delete_comment_check(request, pk):
        target_comment = get_object_or_404(Comment, pk=pk)
        target_comment.delete()
        return HttpResponseRedirect(reverse('blogapp:index'))
    else:
        return HttpResponseRedirect(reverse('blogapp:index'))
