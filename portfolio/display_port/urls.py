from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^index/', index, name="index"),
	url(r'^zen_garden/', zen_garden, name="zen_garden"),
]