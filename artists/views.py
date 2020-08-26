from django.shortcuts import render
from .models import Artist
# Create your views here.
def artists(request, name = None):

	artists = Artist.objects.all()

	return render(request, "artists.html", {
		"artists": artists,
		"name": name
		})