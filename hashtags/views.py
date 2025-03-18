from django.shortcuts import render
from  . import models

def all_category_film(request):
    if request.method == 'GET':
        query = models.Post.objects.all()
        return render(request,
        template_name='tags/all_category_film.html',
        context={'query': query}
                      )

def comics_category_film(request):
    if request.method == 'GET':
        query = models.Post.objects.all().filter(tags__name__contains='comics film')
        return render(request,
                      template_name='tags/comics_category_film.html',
                      context={'query': query}
                      )

def comedy_category_film(request):
    if request.method == 'GET':
        query = models.Post.objects.all().filter(tags__name__contains='comedy')
        return render(request,
                      template_name='tags/comedy_category_film.html',
                      context={'query': query}
                      )