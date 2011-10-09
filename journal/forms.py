
from django.forms import ModelForm
from journal.models import Journal

class JournalForm(ModelForm):
  class Meta:
    model = Journal
    # fields = ('pdf', )
