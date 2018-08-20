from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import BlogPost, Comment
# Create your views here.

def index(request):
    blogpost_list = BlogPost.objects.all()
    context = {'blogposts':blogpost_list}
    return render(request, 'blogapp/index.html', context)
