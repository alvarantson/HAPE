from django.db import models
import string
import random

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
	exists = True
	while exists == True:
		ran = ''.join(random.choice(chars) for _ in range(size))
		if len(Item.objects.filter(random_str=ran)) == 0:
			exists = False

	return ran



# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=999, unique=True)
	description = models.TextField(blank=True)
	random_str = models.CharField(max_length=999, default=id_generator)

	original_price = models.FloatField()
	markup_percentage = models.PositiveIntegerField(default=120)
	price = models.FloatField(blank=True) 
	discount_percentage = models.PositiveIntegerField(default=0)

#TODO suurused


	img = models.ImageField()
	img_2 = models.ImageField(null=True, blank=True)
	img_3 = models.ImageField(null=True, blank=True)
	img_4 = models.ImageField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.price is None:
			self.price = self.original_price * self.markup_percentage / 100
		super(Item, self).save(*args, **kwargs)

	def __str__(self):
		if self.discount_percentage == 0:
			return self.name + " - " + str(self.price) + "€"
		else:
			return self.name + " - " + str( self.price*((100-self.discount_percentage)/100) ) + "€ - DISCOUNT " + str(self.discount_percentage) + "%"