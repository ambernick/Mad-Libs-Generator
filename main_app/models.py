from django.db import models
from django.urls import reverse
# Create your models here.
class MadLib(models.Model):
  title = models.CharField(max_length=250, null=True)
  wordinserts = models.TextField(max_length=100, null=True)
  story = models.TextField(max_length=500, null=True)
  theme = models.CharField(max_length=250, null=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'madlib_id': self.id})
