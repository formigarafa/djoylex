from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import User

def index(request):
  current_user_id = request.session.get('user_id')
  if current_user_id:
    user = User.objects.get(id=current_user_id)
  else:
    user = None
  ids = range(1,10)
  return render_to_response('index.html', {'ids': ids, 'user': user, 'user_id': current_user_id})

def show(request, id):
  return render_to_response('show.html', {'id': id})

def new(request):
  return render_to_response('new.html')

def create(request):
  return HttpResponse('create')

def edit(request, id):
  return render_to_response('edit.html', {'id': id})

def update(request, id):
  return HttpResponse('update: (id: '+id+')')

def destroy(request, id):
  return HttpResponse('destroy: (id: '+id+')')

