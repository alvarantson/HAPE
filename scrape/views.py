from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .scrape_videos import *


# Create your views here.
def scrape(request):
	if request.user.is_superuser:

		if request.POST:
			if "update-views" in request.POST["submit-btn"]:
				videos_stats_update()

			elif "update-releases" in request.POST["submit-btn"]:
				video_upload_update()

		a = []
		for channel in Channel.objects.all():
			b = []
			for video in Video.objects.filter(channel=channel):
				b.append({"video": video, "stats": Video_history.objects.filter(video=video).order_by("-date")})
			a.append({"channel":channel, "videos":b})



		return render(request, "scrape.html", {"channels":a})
	else:
		return HttpResponseRedirect("/")