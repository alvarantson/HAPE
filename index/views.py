from django.shortcuts import render
from artists.models import Artist
from releases.models import Release
from shop.models import Item
# Create your views here.
def index(request):

	artists = Artist.objects.all()
	releases = Release.objects.all().order_by('-date')[:3]
	merch = Item.objects.all()[:9]


	return render(request, "index.html", {
		'artists': artists,
		'releases': releases,
		'merch': merch
		})