from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


def film_detail(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Films, id=id)
        return render(
            request,
            template_name='show_detail.html',
            context={
                'film_id': film_id,
            }
        )

def films_list(request):
    if request.method == 'GET':
        query = models.Films.objects.all()
        return render(
            request,
            template_name='show.html',
            context={
                'query': query,
            }
        )




def emodji(request):
    if request.method == "GET":
        return HttpResponse('😁')

def text(request):
    if request.method == "GET":
        return HttpResponse("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

def image(request):
    if request.method == "GET":
        return HttpResponse("<img src='https://www.bethowen.ru/upload/iblock/898/8982eee1d576c30e28811046c021a8af.jpg' >")



