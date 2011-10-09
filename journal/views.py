
from django.shortcuts import render_to_response, get_object_or_404

def add(request):
  return render_to_response('add.html')

def show(request, journal_id):
  return render_to_response('view.html', { 'id': journal_id })
