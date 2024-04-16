from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from . models import *
from django.views import generic
from .forms import SignupForm, LoginForm, CommentForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from blog.mailer import Mailer

# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

# blog post list
def blog_post_list(request):
    posts = Blog.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})

# share blog through email
def blog_post_email(request, pk):
    posts = Blog.objects.get(id=pk)
    subject = "share blog through email"
    message = "Dear" + " " + str(posts.author.first_name)  + " " +  str(posts.author.last_name)
    mail_response = Mailer(email_id=posts.author.email, subject=subject, otp=message,  type="blog", content=posts.content, title=posts.title)
    _mail= mail_response()
    return render(request, 'blog_list.html', {'posts': posts})

def search(request):
    query = request.GET.get('q')
    blogs = Blog.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'blog_search.html', {'blogs': blogs})


def tag_search(request, tag):
    blogs = Blog.objects.filter(tags__name__icontains=tag)
    return render(request, 'blog_tag_search.html', {'blogs': blogs})

def post_detail(request, slug):
    template_name = 'blog_detail.html'
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

