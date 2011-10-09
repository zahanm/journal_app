
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from journal.forms import JournalForm

def add(request):
  if request.method == 'POST':
    form = JournalForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = JournalForm()
  return render_to_response('add.html', { 'form': form }, context_instance=RequestContext(request))

def show(request, journal_id):
  return render_to_response('view.html', { 'id': journal_id })
