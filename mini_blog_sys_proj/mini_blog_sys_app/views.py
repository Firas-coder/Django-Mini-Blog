from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm, categryForm
from django.contrib import messages
# Create your views here.
def all_posts_search(request):
    all_posts = Post.objects.all()
    all_categories = Category.objects.all()
   
    if request.method == 'GET':
        search_title = request.GET.get('search_title', '')
        search_category = request.GET.get('search_category', '')

        if search_title or search_category:
            all_posts = Post.objects.filter(title__icontains=search_title).order_by('-created_at')
            all_posts = all_posts.filter(category__name__icontains=search_category).order_by('-created_at')
        elif search_title or search_category == '':
            messages.error(request, "Search Title and Search Category cannot be empty.")    
        else:
            messages.error(request, "Invalid search Title Or Search Category.")
            
    context={
        'all_posts': all_posts,
        'all_categories': all_categories,
        'message': messages.get_messages(request)
    }
    return render(request, 'pages/all_p.html', context)
def add_post(request):
    if request.method =='POST':
        add_postform = PostForm(request.POST)
        if add_postform.is_valid():
            add_postform.save()
            return redirect('all_posts_search')
    else:
        add_postform = PostForm()
    return render(request, 'pages/add_p.html', {'add_postform': add_postform})
def edit_post(request, post_id):
    if request.method=='POST':
        post = Post.objects.get(id=post_id)
        edit_postform = PostForm(request.POST, instance=post)
        if edit_postform.is_valid():
            edit_postform.save()
            return redirect('all_posts_search')
    else:
        post = Post.objects.get(id=post_id)
        edit_postform = PostForm(instance=post)
    return render(request, 'pages/edit_p.html', {'edit_postform': edit_postform})
def delete_post(request, post_id):
    if request.method=='POST':
        post_id = Post.objects.get(id=post_id)
        post_id.delete()
        return redirect('all_posts_search')  
    else:
        post_id = Post.objects.get(id=post_id)
    return render(request, 'pages/delete_p.html', {'post_id': post_id})  
def add_category(request):
    if request.method=='POST':
        add_categryform= categryForm(request.POST)
        if add_categryform.is_valid():
            add_categryform.save()
            return redirect('add_post')
    else:
            add_categryform = categryForm()
    return render(request, 'pages/add_cat.html', {'add_categoryform': add_categryform})
