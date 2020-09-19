from django.db import models

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=999, unique=True)
	real_name = models.CharField(max_length=999, blank=True)
	email = models.CharField(max_length=999, blank=True)
	description = models.TextField(blank=True)

	front_page_priority = models.IntegerField(unique=True, blank=True)

	yt_url = models.CharField(max_length=999, blank=True)
	sc_url = models.CharField(max_length=999, blank=True)
	sp_url = models.CharField(max_length=999, blank=True)
	it_url = models.CharField(max_length=999, blank=True)
	ig_url = models.CharField(max_length=999, blank=True)
	fb_url = models.CharField(max_length=999, blank=True)

	front_page_img = models.ImageField(null=True)
	artist_page_img = models.ImageField(null=True)
	artist_page_bg = models.ImageField(null=True)

	artist_page_font_color = models.CharField(max_length=999, blank=True)
	artist_page_shadow = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.name