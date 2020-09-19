from django.shortcuts import render
from .models import Artist
# Create your views here.
def artists(request, name = None):

	artists = []
	a = Artist.objects.all()
	for i in range(int(len(a)/2)+1):
		pair = []
		try:
			pair.append(a[i*2])
			pair.append(a[i*2+1])
			artists.append(pair)
		except:
			print(pair)
			artists.append(pair)
			


	return render(request, "artists.html", {
		"artists": artists,
		"name": name
		})