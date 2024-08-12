from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, Categorys,About
from .forms import Contact_forms
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    blog_title = 'Latest post'
    posts = Post.objects.all()
    paginator = Paginator(posts,5)
    pages= request.GET.get('page')
    page_obj= paginator.get_page(pages)
    return render(request,'index.html', {'blog_title': blog_title, 'posts':page_obj})

def detail(request, slug):
    posts = Post.objects.get(slug = slug)
    related_post= Post.objects.filter(category = posts.category)

    return render(request,'details.html',{'post':posts,'related_posts':related_post})

def contacts(request):
    if request.method == 'POST':
        form = Contact_forms(request.POST)
        if form.is_valid():
            success_message = "your email has been sent successfully"

        return render(request,'contacts.html',{'form':form, 'success_message':success_message})
    return render(request,'contacts.html')

def about(request):
    about_content= About.objects.first().content
    return render(request,'about.html',{'about_content':about_content})
