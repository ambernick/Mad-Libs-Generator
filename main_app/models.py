from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class MadLib(models.Model):
  title = models.CharField(max_length=250, null=True)
  wordinserts = models.TextField(max_length=100, null=True)
  story = models.TextField(max_length=5000, null=True)
  theme = models.CharField(max_length=250, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'madlib_id': self.id})
