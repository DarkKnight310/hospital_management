# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response, render
from manageHospital import models
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.views.decorators.csrf import csrf_protect
from manageHospital.models import *



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

def receptionist_existing_patient(request):
	if request.method == 'POST':
		form = patient_existing_det(request.POST)
		if form.is_valid():
			r_id = request.session['user_id']
			r_obj = receptionist.objects.get(receptionist_login = r_id)
			p_id = form.cleaned_data['patient']
			p_object = patients.objects.get(id = p_id)
			#rm_id = form.cleaned_data['patient_room_no']
			#rm_obj = room.objects.get(id = rm_id)
			a = appointment(receptionist_id = r_obj, patient_id = p_object, patient_date_of_admission = form.cleaned_data['patient_date_of_admission'],patient_problem = form.cleaned_data['patient_problem'], treated = False)
			a.save()
			d_id = form.cleaned_data['doctors_available']
			d_object = doctors.objects.get(id = d_id)
			d_object.doctor_availability = False
			d_object.save()

			c = consults(appointment_id = a,doctor_id = d_object, allot_room = False, prescription = "null")
			c.save()

			return HttpResponseRedirect('/login/receptionist/home')
	else:
		form = patient_existing_det()
	return render(request, 'patient_det_form.html', {'form': form})

def receptionist_edit_appointment(request, appointment_id):
	if request.method == 'POST':
		a = appointment.objects.get(id=appointment_id)
		if a.treated == True:
			form = appointment_edit_treated(request.POST)
			if form.is_valid():
				patient_room_no = form.cleaned_data['patient_room_no']
				r = room.objects.get(id=patient_room_no)
				a.room_id = r
				a.save()
				return HttpResponseRedirect('/login/receptionist/home')

		else:
			form = appointment_edit(request.POST)
			#print ("sdfsvv")
			if form.is_valid():
				#print ("hahaha")
				patient_date_of_admission = form.cleaned_data['patient_date_of_admission']
				patient_problem = form.cleaned_data['patient_problem']
				choice = form.cleaned_data['choice']
				a.patient_problem = patient_problem
				a.patient_date_of_admission = patient_date_of_admission
				#print (choice)
				if choice == "1":
					#print ("aya")
					c = consults.objects.get(appointment_id = a)
					d = c.doctor_id
					d.doctor_availability = True
					d.save()
					c.delete()
					a.save()
					d_id = form.cleaned_data['doctors_available']
					#print ("IUGIBJFNSJN")
					#print (d_id)
					d_object = doctors.objects.get(id = d_id)
					d_object.doctor_availability = False
					d_object.save()
					c = consults(appointment_id = a,doctor_id = d_object, allot_room = False, prescription = "null")
					c.save()
				else:
					a.save()
				return HttpResponseRedirect('/login/receptionist/home')
	else:
		a = appointment.objects.get(id=appointment_id)
		p = patients.objects.get(id = a.patient_id.id)
		c = consults.objects.get(appointment_id = a)
		d = c.doctor_id
		if a.treated == True and c.allot_room == True:
			try:
				form = appointment_edit_treated(initial={'patient_room_no': a.room_id.id})
			except:
				form = appointment_edit_treated()
			return render(request, 'edit_appointment_treated.html', {'p': p, 'form': form})
		elif a.treated == True: 
			return render(request, 'error_room_not_alloted.html')
		else:
			form = appointment_edit(initial={'patient_problem': a.patient_problem, 'patient_date_of_admission': a.patient_date_of_admission})
			return render(request, 'edit_appointment.html', {'p': p, 'form': form, 'd': d})

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
		try:
			x = consults.objects.get(appointment_id=i, doctor_id=q0)
			c1.append(x)
		except:
			print ("hii")
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
			user_id = request.session['user_id']
			q0 = doctors.objects.get(doctor_login = user_id)
			q0.doctor_availability = True
			q0.save()
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
			a0 = appointment.objects.get(id = a_id)
			q0 = consults.objects.get(appointment_id = a0)
			print(q0.doctor_id)
			d0 = doctors.objects.get(pk = q0.doctor_id.id)
			d_fees = d0.doctor_consultation_fee
			r_cost = d_fees
			if q0.allot_room == True:
				r0 = room.objects.get(id = a0.room_id.id)
				tdelta = datetime.today().date() - a0.patient_date_of_admission.date()
				days = tdelta.days
				print(r0.charge)
				print(days)
				r_cost = d_fees + (days*r0.charge)
			bill_up = bill(appointment_id = a0, discharge_time = datetime.now(), amount = r_cost)
			bill_up.save()
			print(r_cost)
			return HttpResponseRedirect('/login/receptionist/bill_print/{}'.format(a_id))
	else:
		form = bill_inf()
	return render(request, 'bill.html', {'form': form})

#as soon as bill is generated,it prints it			

def bill_print(request, a_id):
	
	a0 = appointment.objects.get(id = a_id)
	q0 = consults.objects.get(appointment_id = a0)
	print(q0.doctor_id)
	d0 = doctors.objects.get(pk = q0.doctor_id.id)
	d_fees = d0.doctor_consultation_fee
	r_cost = d_fees
	if q0.allot_room == True:
		r0 = room.objects.get(id = a0.room_id.id)
		tdelta = datetime.today().date() - a0.patient_date_of_admission.date()
		days = tdelta.days
		print(r0.charge)
		print(days)
		r_cost = d_fees + (days*r0.charge)
	return render(request, 'bill_print.html', {'appid': a_id,'pat_id': a0.patient_id.id, 'doc_id':q0.doctor_id.id, 'doc_name':q0.doctor_id.doctor_name,'final_amount':r_cost, 'r_id':a0.room_id.id,'r_charge':r0.charge})		

#showing bill info given by bill_id, urls update karde

def get_bill_print(request, b_id):
	
	b0 = bill.objects.get(id = b_id)
	a0 = appointment.objects.get(id = b0.appointment_id.id)
	q0 = consults.objects.get(appointment_id = a0)
	print(q0.doctor_id)
	d0 = doctors.objects.get(pk = q0.doctor_id.id)
	d_fees = d0.doctor_consultation_fee
	r_cost = d_fees
	if q0.allot_room == True:
		r0 = room.objects.get(id = a0.room_id.id)
		tdelta = datetime.today().date() - a0.patient_date_of_admission.date()
		days = tdelta.days
		print(r0.charge)
		print(days)
		r_cost = d_fees + (days*r0.charge)
	return render(request, 'bill_print.html', {'appid': appointment_id.id,'pat_id': a0.patient_id.id, 'doc_id':q0.doctor_id.id, 'doc_name':q0.doctor_id.doctor_name,'final_amount':r_cost, 'r_id':a0.room_id.id,'r_charge':r0.charge})		