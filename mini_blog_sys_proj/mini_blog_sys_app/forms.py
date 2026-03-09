from django import forms
from .models import Post, Category
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
            'category': 'Post Category'
        }
        help_texts = {
            'title': 'Enter the title of your post.',
            'content': 'Write the content of your post here.',
            'category': 'Select a category for your post.'
        }
class categryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'name': 'Enter the name of the category.',
        }