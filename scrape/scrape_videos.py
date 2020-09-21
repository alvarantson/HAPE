
import time
import re
from robobrowser import RoboBrowser
from werkzeug.utils import cached_property

from .models import *

def video_scrape(channel):
	browser = RoboBrowser(history=True)
	browser.open(channel.url.replace("/featured","")+"/videos")
	time.sleep(.1)
	for link in re.findall("/watch\?v=[a-zA-Z0-9_-]+", str(browser.parsed)):
		if len(Video.objects.filter(channel=channel, url="https://www.youtube.com"+link)) == 0:
			br = RoboBrowser(history=True)
			br.open("https://www.youtube.com"+link)
			time.sleep(.3)
			name = re.findall("meta content=\"(.+)\" name=\"twitter:title", str(br.parsed))[0]
			Video.objects.create(channel=channel, name=name, url="https://www.youtube.com"+link)

def stats_scrape(video):
	browser = RoboBrowser(history=True)
	browser.open(video.url)
	time.sleep(.1)
	views = (re.findall("\"viewCount\":(.+)", str(browser.parsed))[0].split(" vaatamist")[0].split("\"")[-1])
	likes = (re.findall("(\d+) meeldimist", str(browser.parsed)))[0]
	dislikes = (re.findall("(\d+) kasutajale ei meeldinud", str(browser.parsed)))[0]

	views = str(views).replace(u'\xa0', u'')
	likes = str(likes).replace(u'\xa0', u'')
	dislikes = str(dislikes).replace(u'\xa0', u'')
	
	Video_history.objects.create(video=video,views=int(views),likes=int(likes),dislikes=int(dislikes))

def videos_stats_update():
	for video in Video.objects.all():
		stats_scrape(video)

def video_upload_update():
	for channel in Channel.objects.all():
		video_scrape(channel)