from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

def post_list(request):

    u = User.objects.get(username='admin')

    posts = Post.objects.filter(author=u).order_by('published_date')
    return render(request, 'blogum/post_list.html', {'posts': posts})