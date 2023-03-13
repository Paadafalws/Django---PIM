from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.shortcuts import render

def members(request):
  template = loader.get_template('home.html') #AKI QUE COMANDA ONDE VOCE TEM QUE IR PARA ESSA POHA DE SITGE
  return HttpResponse(template.render())

