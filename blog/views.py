from django.shortcuts import render
from .models import AuthorModel, PostModel

# Create your views here.
def homepage(request):
    authors = AuthorModel.objects.all()
    posts = PostModel.objects.all()
    context = {
        'authors' :authors,
        'posts': posts
    }
   
    return render(request, "blog/homepage.html", context)