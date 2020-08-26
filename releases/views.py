from django.shortcuts import render
from .models import Release
# Create your views here.
def releases(request):

	releases = Release.objects.all().order_by('-date')

	return render(request, "releases.html", {
		"releases":releases
		})