from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    myImages = Movie.objects.all()
    context = {'myImages': myImages}
    return render(request, 'disneyapp/index.html', context)

def tvshow(request):
    context = {}
    return render(request, 'disneyapp/tvshow.html', context)

def movies(request):
    context = {}
    return render(request, 'disneyapp/movies.html', context)

