from django.http import HttpResponse

def index(request):
  return HttpResponse('index')
  
def show(request, id):
  return HttpResponse('show: (id: '+id+')')