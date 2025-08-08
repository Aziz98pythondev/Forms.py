from django.shortcuts import render, redirect

from .forms import AboutUsForm
from .models import AboutUs

def about_form(request):
    form = AboutUsForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect('about_list')
    
    context = {
        'form': form
    }

    return render(request, 'form.html', context)

def about_list(request):
    about = AboutUs.objects.all()

    context = {
        'about':about
    }
    
    return render(request, 'home.html', context)