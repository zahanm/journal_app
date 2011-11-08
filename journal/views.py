
from django.shortcuts import render, get_object_or_404, redirect

from journal.forms import JournalForm
from manipulation.pdfsplit import split_pdf

def add(request):
  if request.method == 'POST':
    form = JournalForm(request.POST, request.FILES)
    if form.is_valid():
      journal = form.save()
      split_pdf(journal.pdf)
      return redirect('home')
  else:
    form = JournalForm()
  return render(request, 'add.html', { 'form': form })

def show(request, journal_id):
  return render(request, 'view.html', { 'id': journal_id })
