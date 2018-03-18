from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^doctor/$', views.get_name),
	url(r'^receptionist/$', views.receptionistlogin),
	url(r'^$', views.first_page),
]
