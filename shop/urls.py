from django.urls import path, re_path
from . import views

urlpatterns = [
	path("", views.shop),
	re_path(r'(?P<random_str>.*)/$', views.item_view),
]