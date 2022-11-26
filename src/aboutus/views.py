from django.shortcuts import render
from .models import AboutUs, Why_Choose_US, Chef
# Create your views here.

def aboutus_list(request):
    about = AboutUs.objects.last()
    why_choose_us = Why_Choose_US.objects.all()
    chef = Chef.objects.all()

    context = {
        'sobre' : about,
        'why_choose_us' : why_choose_us,
        'chef' : chef,
    }
    print(about)
    return render(request, 'Aboutus/about.html', context)

