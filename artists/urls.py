from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.artists),
	re_path(r'(?P<name>.*)/$', views.artists),
]