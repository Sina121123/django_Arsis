from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts
from django.views.generic import TemplateView


def post_list(request):
    posts = Posts.objects.all()
    context = {
         'posts' : posts
    }
    return render(request,'html/index.html',context)