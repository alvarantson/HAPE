from django.shortcuts import render
from .models import Item
# Create your views here.
def shop(request):

	merch = Item.objects.all()

	return render(request, "shop.html", {
		"merch": merch
		})

def item_view(request, random_str):

	item = Item.objects.get(random_str=random_str)

	return render(request, "item_view.html", {
		"item": item
		})