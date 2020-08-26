from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import stripe
from django.conf import settings
from LEHT.settings import BASE_DIR
from datetime import datetime
# Create your views here.
