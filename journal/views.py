
from django.http import HttpResponse

def add(request):
  return HttpResponse('Added journal')

def show(request, journal_id):
  return HttpResponse('Show journal with id {0}'.format(journal_id))
