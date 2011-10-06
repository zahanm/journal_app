
from django.db import models

class Journal(models.Model):
  name = models.CharField(max_length=100)
  pdf = models.FileField()

TYPES_OF_SECTIONS = (
  ('text', 'text transcription'),
  ('math', 'equations and LaTeX')
)

class Section(models.Model):
  auto_id = models.AutoField()
  img = models.ImageField()
  trans_type = models.CharField(max_length=4, choices=TYPES_OF_SECTIONS)
  transcription = models.TextField(default='')
