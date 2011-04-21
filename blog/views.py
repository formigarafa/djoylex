from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def show(request, id):
  return render(request, 'show.html', {'id': id})

def new(request):
  return render(request, 'new.html')

def create(request):
  return HttpResponse('create')

def edit(request, id):
  return render(request, 'edit.html', {'id': id})

def update(request, id):
  return HttpResponse('update: (id: '+id+')')

def destroy(request, id):
  return HttpResponse('destroy: (id: '+id+')')
