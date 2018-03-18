from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^doctor/$', views.doctor_login),
	url(r'^receptionist/$', views.receptionist_login),
	url(r'^$', views.first_page),
	url(r'^doctor/home/$', views.doctor_home),
	url(r'^receptionist/home/$', views.receptionist_home),
]
