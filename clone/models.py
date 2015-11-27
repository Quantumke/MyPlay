from django.db import models
import operator
from django.db.models import permalink

# Create your models here.
class Dplay(models.Model):
	title = models.CharField(max_length=100, unique=False)
	description = models.CharField(max_length=100, unique=False)
	thumbnail=models.CharField(max_length=100, unique=False)
	video = models.CharField(max_length=100, unique=False)
	uploaded_by=models.CharField(max_length=100, unique=False)
	date = models.DateField(max_length=100, unique=False)
	views=models.CharField(max_length=100, unique=False)
	category=models.CharField(max_length=100, unique=False)
	channel=models.CharField(max_length=100, unique=False)
	slug = models.SlugField(max_length=100, unique=True)
	def __unicode__(self):
		return '%s' %self.title
	@permalink
	def get_absolute_url(self):
		return('view_more', None, {'slug':self.slug})
