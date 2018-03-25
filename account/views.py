# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, render
from manageHospital import models
from django.http import HttpResponseRedirect, HttpResponse
from .forms import login, pres, patient_det
from django.views.decorators.csrf import csrf_protect
from manageHospital.models import login_details, patients, consults, doctors, appointment, receptionist



# Create your views here.

def first_page(request):
	return render_to_response('first_page.html')

def receptionist_login(request):
	if request.method == 'POST':
		request.session['user_id']=""
		form = login(request.POST)
		if form.is_valid():
			user_id = form.cleaned_data['user_id']
			user_pwd = form.cleaned_data['user_pwd']
			matched = login_details.objects.filter(type = '2', username = user_id, password = user_pwd)
			if len(matched) is 1:
				request.session['user_id'] = user_id
				return HttpResponseRedirect('home/')
	else:
		request.session['user_id']=""
		form = login()
	user_type = "Receptionist"
	return render(request, 'login_withform.html', {'user_type': user_type, 'form': form})

def receptionist_home(request):
	user_id = request.session['user_id']
	q0 = receptionist.objects.get(receptionist_login = user_id)
	name = q0.receptionist_name
	q3 = q0.appointment_set.all()
	data=[]
	for i in q3:
		x = i, patients.objects.get(id = i.patient_id.id)
		data.append(x)
	return render_to_response('receptionist_home.html', {'name': name, 'data': data})

def receptionist_new_patient(request):
	if request.method == 'POST':
		form = patient_det(request.POST)
		if form.is_valid():
			r_id = request.session['user_id']
			r_obj = receptionist.objects.get(receptionist_login = r_id)
			q = patients(patient_name= form.cleaned_data['patient_name'], patient_city_name=form.cleaned_data['patient_city_name'], patient_house_no=form.cleaned_data['patient_house_no'], patient_street_no = form.cleaned_data['patient_street_no'], patient_age = form.cleaned_data['patient_age'],patient_gender = form.cleaned_data['patient_gender'])
			q.save()
			#rm_id = form.cleaned_data['patient_room_no']
			#rm_obj = room.objects.get(id = rm_id)
			a = appointment(receptionist_id = r_obj, patient_id = q, patient_date_of_admission = form.cleaned_data['patient_date_of_admission'],patient_problem = form.cleaned_data['patient_problem'], treated = False)
			a.save()
			d_id = form.cleaned_data['doctors_available']
			d_object = doctors.objects.get(id = d_id)
			d_object.doctor_availability = False
			d_object.save()

			c = consults(appointment_id = a,doctor_id = d_object, allot_room = False, prescription = "null")
			c.save()

			return HttpResponseRedirect('/login/receptionist/home')
	else:
		form = patient_det()
	return render(request, 'patient_det_form.html', {'form': form})


def doctor_home(request):
	user_id = request.session['user_id']
	q0 = doctors.objects.get(doctor_login = user_id)
	name = q0.doctor_name;
	q3 = q0.consults_set.all()
	data=[]
	#p=[]
	for i in q3:
		try:
			x = appointment.objects.get(id = i.appointment_id.id)
			p=(appointment.objects.filter(id = i.appointment_id.id)[0],patients.objects.filter(id = x.patient_id.id)[0])
			data.append(p)
		except:
			print ("hi")
		#print (p[1].patient_gender)
	new_patient = []
	try:
		c1 = q3[len(q3) - 1]
		new_patient = appointment.objects.get(id=c1.appointment_id.id, treated = False)
	except:
		print ("hi")
	return render_to_response('doctor_home.html', {'name': name, 'data': data, 'new_patient': new_patient})

def doctor_login(request):
	if request.method == 'POST':
		request.session['user_id']=""
		form = login(request.POST)
		if form.is_valid():
			user_id = form.cleaned_data['user_id']
			user_pwd = form.cleaned_data['user_pwd']
			matched = login_details.objects.filter(type = '1', username = user_id, password = user_pwd)
			if len(matched) is 1:
				request.session['user_id'] = user_id
				return HttpResponseRedirect('home/')
	else:
		request.session['user_id']=""
		form = login()
	user_type = "Doctor"
	return render(request, 'login_withform.html', {'user_type': user_type, 'form': form})

def patient_doctor(request,patient_id):
	p = patients.objects.get(id = patient_id)
	user_id = request.session['user_id']
	q0 = doctors.objects.get(doctor_login = user_id)
	c = appointment.objects.filter(patient_id = p)
	a = []
	c1 = []
	for i in c:
		c1.append(consults.objects.get(appointment_id=i, doctor_id=q0))
	for i in c1:
		print(i)
		pp=(i,appointment.objects.get(id=i.appointment_id.id))
		a.append(pp)
	return render_to_response('patient_doctor.html', {'patient': p, 'a': a})

def prescription(request, appointment_id):
	if request.method == 'POST':
		form = pres(request.POST)
		if form.is_valid():
			presc = form.cleaned_data['prescription']
			allot_room = form.cleaned_data['allot_room']
			user_id = request.session['user_id']
			q0 = doctors.objects.get(doctor_login = user_id)
			a = appointment.objects.get(id=appointment_id)
			c_edit = consults.objects.get(appointment_id = a)
			c_edit.allot_room = allot_room
			c_edit.prescription = presc
			c_edit.save()
			a.treated = True
			a.save()
			return HttpResponseRedirect('/login/doctor/home/')
	else:
		form = pres()
	a = appointment.objects.get(id=appointment_id)
	p = patients.objects.get(id = a.patient_id.id)
	return render(request, 'prescription.html', {'a': a, 'p': p, 'form': form})

def patient_info(request):
	if request.method == 'POST':

		form = patient_det(request.POST)
		if form.is_valid():
			q = patients(patient_name= form.cleaned_data['patient_name'], patient_city_name=form.cleaned_data['patient_city_name'], patient_house_no=form.cleaned_data['patient_house_no'], patient_street_no = form.cleaned_data['patient_street_no'], patient_age = form.cleaned_data['patient_age'],patient_gender = form.cleaned_data['patient_gender'])
			q.save()	
			a = appointment(receptionist_id = user_id, patient_id = q.id, room_id = -1, patients_date_of_admission = form.cleaned_data['patients_date_of_admission'],patient_problem = form.cleaned_data['patient_problem'], treated = False)		
			a.save()
			#print("hi")
			#update by rungta
			c = consults(appointment_id = a.id,doctor_id = form.cleaned_data['doctors_available'],allot_room = False, prescription = "Enter the prescription here")
			c.save()
			return HttpResponseRedirect('/login/receptionist')
	else:
		form = patient_det()
	return render(request, 'patient_det_form.html', {'form': form})

def bill_info(request):
	if request.method == 'POST':
		form = bill_inf(request.POST)
		if form.is_valid():
			a_id = form.cleaned_data['appointment_id']
			q0 = consults.objects.get(appointment_id = a_id)
			d0 = doctors.objects.get(id = q0.doctor_id)
			#a0 = appointment.objects.get(id = a_id)
			#r0 = room.objects.get(id = a0.room_id)
			r_cost = r0.charge
			d_fees = d0.doctor_consultation_fee
			if q0.allot_room == True:
				a0 = appointment.objects.get(id = a_id)
				r0 = room.objects.get(id = a0.room_id)
				tdelta = timezone.now() - a0.receptionist_date_of_joining
				hrs = tdelta.seconds/3600
				days = hrs/24
				r_cost = r_cost + (days*r0.charge)

			bill_up = bill(appointment_id = a_id, discharge_time = timezone.now(), amount = r_cost)
			return HttpResponseRedirect('/login/receptionist')
	else:
		form = patient_det()
	return render(request, 'patient_det_form.html', {'form': form})