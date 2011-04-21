from django.http import HttpResponse

def index(request):
  return HttpResponse('index')
  
def show(request, id):
  return HttpResponse('show: (id: '+id+')')

def new(request):
  return HttpResponse('new')

def create(request):
  return HttpResponse('create')

def edit(request, id):
  return HttpResponse('edit: (id: '+id+')')

def update(request, id):
  return HttpResponse('update: (id: '+id+')')

def destroy(request, id):
  return HttpResponse('destroy: (id: '+id+')')
