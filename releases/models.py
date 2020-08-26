from django.db import models
import string
import random

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
	exists = True
	while exists == True:
		ran = ''.join(random.choice(chars) for _ in range(size))
		if len(Release.objects.filter(random_str=ran)) == 0:
			exists = False

	return ran

# Create your models here.
class Release(models.Model):
	name = models.CharField(max_length=999, blank=True)
	artists = models.CharField(max_length=999, blank=True)
	random_str = models.CharField(max_length=999, default=id_generator)

	date = models.DateField(blank=True)

	yt_embed = models.CharField(max_length=999, blank=True)

	yt_url = models.CharField(max_length=999, blank=True)
	sc_url = models.CharField(max_length=999, blank=True)
	sp_url = models.CharField(max_length=999, blank=True)
	it_url = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.name + " - " + self.artists