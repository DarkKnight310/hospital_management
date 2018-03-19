# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, render
from manageHospital import models
from django.http import HttpResponseRedirect, HttpResponse
from .forms import login
from django.views.decorators.csrf import csrf_protect
from manageHospital.models import login_details, patients, consults, doctors



# Create your views here.

def first_page(request):
	return render_to_response('first_page.html')

def doctorlogin(request):
	user_type = "Doctor"
	return render_to_response('login.html', {'user_type': user_type})

def receptionistlogin(request):
	user_type = "Receptionist"
	return render_to_response('login.html', {'user_type': user_type})

def receptionist_home(request):
	return render_to_response('receptionist_home.html')

def doctor_home(request):
	user_id = request.session['user_id']
	q0 = doctors.objects.get(doctor_login = user_id)
	name = q0.doctor_name;
	q3 = q0.consults_set.all()
	data=[]
	for i in q3:
		data.append(patients.objects.get(id = i.patient_id.id))
	return render_to_response('doctor_home.html', {'name': name, 'data': data})

def doctor_login(request):
	if request.method == 'POST':
		form = login(request.POST)
		if form.is_valid():
			user_id = form.cleaned_data['user_id']
			user_pwd = form.cleaned_data['user_pwd']
			matched = login_details.objects.filter(type = '1', username = user_id, password = user_pwd)
			if len(matched) is 1:
				request.session['user_id'] = user_id
				return HttpResponseRedirect('home/')
	else:
		form = login()
	user_type = "Doctor"
	return render(request, 'login_withform.html', {'user_type': user_type, 'form': form})

def receptionist_login(request):
	if request.method == 'POST':
		form = login(request.POST)
		if form.is_valid():
			user_id = form.cleaned_data['user_id']
			user_psw = form.cleaned_data['user_pwd']
			if user_id == "jin":
				return HttpResponseRedirect('home/')
	else:
		form = login()
	user_type = "Receptionist"
	return render(request, 'login_withform.html', {'user_type': user_type, 'form': form})