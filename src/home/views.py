from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from aboutus.models import Why_Choose_US
# Create your views here.

def home(request):

    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    why_choose_us = Why_Choose_US.objects.all()

    context = {
        'meal_list' : meal_list,
        'categories' : categories,
        'posts' : posts,
        'latest_post' : latest_post,
        'why_choose_us' : why_choose_us,
    }

    return render(request, 'Home/index.html', context)
