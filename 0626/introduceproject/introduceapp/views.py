import imp
from time import timezone
from django.shortcuts import redirect, render
from .models import Geust
from .forms import GeustModelForm

# Create your views here.
def home(request):
    posts = Geust.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def favorite(request):
    return render(request, 'favorite.html')

def photo(request):
    return render(request, 'photo.html')

def newguest(request):
    if request.method == 'POST':
      form = GeustModelForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = GeustModelForm()
    return render(request, 'newgeust.html', {'form':form})
