
from django.db import models

class Journal(models.Model):
  name = models.CharField(max_length=100)
  pdf = models.FileField(upload_to='uploads')
  def __unicode__(self):
    return self.name

TYPES_OF_SECTIONS = (
  ('text', 'text transcription'),
  ('math', 'equations and LaTeX')
)

class Section(models.Model):
  auto_id = models.AutoField(primary_key=True)
  img = models.ImageField(upload_to='sections')
  trans_type = models.CharField(max_length=4, choices=TYPES_OF_SECTIONS)
  transcription = models.TextField(default='')
  def __unicode__(self):
    return self.trans_type + ': ' + self.img.url
