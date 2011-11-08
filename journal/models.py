
from django.db import models

class Journal(models.Model):
  name = models.CharField(max_length=100)
  pdf = models.FileField(upload_to='journals')
  def __unicode__(self):
    return self.name

TYPES_OF_SECTIONS = (
  ('text', 'text transcription'),
  ('math', 'equations and LaTeX')
)

class Section(models.Model):
  img = models.ImageField(upload_to='sections')
  trans_type = models.CharField(max_length=4, choices=TYPES_OF_SECTIONS)
  transcription = models.TextField(default='')
  journal = models.ForeignKey(Journal) # Journal instance can access sections using j.section_set
  def __unicode__(self):
    return self.trans_type + ': ' + self.img.url
