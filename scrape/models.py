from django.db import models
import string
import random

# Create your models here.

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
	exists = True
	while exists == True:
		ran = ''.join(random.choice(chars) for _ in range(size))
		if len(Channel.objects.filter(random_str=ran)) == 0 and len(Video.objects.filter(random_str=ran)) == 0 and len(Video_history.objects.filter(random_str=ran)) == 0:
			exists = False

	return ran


class Channel(models.Model):
	name = models.CharField(max_length=999)
	url = models.CharField(max_length=999)
	random_str = models.CharField(max_length=999, default=id_generator)

	def __str__(self):
		return self.name

class Video(models.Model):
	channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
	name = models.CharField(max_length=999, blank=True)
	url = models.CharField(max_length=999, blank=True)
	random_str = models.CharField(max_length=999, default=id_generator)

	def __str__(self):
		return self.channel.name + " - " + self.name


class Video_history(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE)

	date = models.DateTimeField(auto_now_add=True, blank=True)

	views = models.IntegerField(blank=True, null=True)
	likes = models.IntegerField(blank=True, null=True)
	dislikes = models.IntegerField(blank=True, null=True)
	comments = models.IntegerField(blank=True, null=True)
	random_str = models.CharField(max_length=999, default=id_generator)

	def __str__(self):
		return self.video.channel.name + " - " + self.video.name + ": " + str(self.date)