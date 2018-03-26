from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
	url(r'^doctor/$', views.doctor_login),
	url(r'^receptionist/$', views.receptionist_login),
	url(r'^$', views.first_page),
	url(r'^doctor/home/$', views.doctor_home),
	url(r'^receptionist/home/$', views.receptionist_home),
	path('doctor/home/patient/<int:patient_id>/', views.patient_doctor),
	path('doctor/home/prescription/<int:appointment_id>/', views.prescription),
	url(r'^receptionist/home/appointment_new/$', views.receptionist_new_patient),
	url(r'^receptionist/home/appointment_exist/$', views.receptionist_existing_patient),
	path('receptionist/home/appointment/<int:appointment_id>/edit', views.receptionist_edit_appointment),
	url(r'^receptionist/bill/$', views.bill_info),
	path('receptionist/view_bill/<int:b_id>',views.get_bill_print),
	url(r'^receptionist/view_bill', views.bill_find),
	path('receptionist/bill_print/<int:a_id>',views.bill_print),
	path('receptionist/home/edit_patient/<int:patient_id>/edit/', views.receptionist_edit_patient),
	url(r'^receptionist/home/patient_edit$', views.patient_edit),
]
