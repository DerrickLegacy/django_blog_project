from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author':'Ahaabwe Derrick',
#         'title': 'How to pass without reading',
#         'content':'First Post Content',
#         'date_posted':'August 28, 2024'
#     },
#     {
#         'author':'Joe Doe',
#         'title': 'Blog Post Two',
#         'content':'Second Post Content',
#         'date_posted':'August 29, 2024'
#     }
# ]

# Create your views here.
# Point/map blog views to templates to render
# Pass Data to views
def home(request):
    context = {
        'posts':Post.objects.all(),
    }    
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
