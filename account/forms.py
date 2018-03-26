from django import forms
from datetime import datetime
from manageHospital.models import *

class login(forms.Form):
    user_id = forms.CharField(label='Login id', max_length=20)
    user_pwd = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput())

class pres(forms.Form):
	prescription = forms.CharField(label='Prescription', max_length=500)
	allot_room = forms.BooleanField(label='Allot Room', required = False)

class patient_det(forms.Form):
	patient_name = forms.CharField(label='Patient-name',max_length=200)
	patient_city_name = forms.CharField(label='City',max_length=200)
	patient_house_no = forms.IntegerField(label='House No.')
	patient_street_no = forms.IntegerField(label='Street No.')
	patient_age = forms.IntegerField(label='Age')
	patient_gender = forms.CharField(label = 'Gender',max_length = 1)
	patient_problem = forms.CharField(label = 'Problem',max_length = 500)
	patient_date_of_admission = forms.DateTimeField(label='date of admission', required = False, initial=datetime.today)
	#patient_room_no = forms.CharField(label = 'Room no',max_length = 5, required = False)
	list1 = doctors.objects.filter(doctor_availability = True)
	print (list1)
	list2 = []
	#print (list1)
	for i in list1:
		x = (i.id, i.doctor_name)
		list2.append(x)
	doctors_available = forms.ChoiceField(choices=[(a, b) for a, b in list2])
	

class patient_existing_det(forms.Form):
	#patient_id = forms.IntegerField(label = 'Patient_id')
	def __init__(self, *args, **kwargs):
		super(patient_existing_det, self).__init__(*args, **kwargs)
		list3 = patients.objects.all()
		list4 = []
		for i in list3:
			y = (i.id, i.patient_name)
			list4.append(y)
		self.fields['patient'] = forms.ChoiceField(label = 'Patient', choices = [(a,b) for a,b in list4])
		self.fields['patient_problem'] = forms.CharField(label = 'Problem',max_length = 500)
		self.fields['patient_date_of_admission'] = forms.DateTimeField(label='date of admission', required = False, initial=datetime.today)
		#self.fields['patient_room_no'] = forms.CharField(label = 'Room no',max_length = 5, required = False)
		list1 = doctors.objects.filter(doctor_availability = True)
		list2 = []
		#print (list1)
		for i in list1:
			x = (i.id, i.doctor_name)
			list2.append(x)
		self.fields['doctors_available'] = forms.ChoiceField(label = 'Doctors Available',choices=[(a, b) for a, b in list2])

class appointment_edit(forms.Form):
	#patient_id = forms.IntegerField(label = 'Patient_id')
	def __init__(self, *args, **kwargs):
		super(appointment_edit, self).__init__(*args, **kwargs)
		self.fields['patient_problem'] = forms.CharField(label = 'Problem',max_length = 500)
		self.fields['patient_date_of_admission'] = forms.DateTimeField(label='date of admission', required = False, initial=datetime.today)
		list1 = doctors.objects.filter(doctor_availability = True)
		list2 = []
		#print (list1)
		for i in list1:
			x = (i.id, i.doctor_name)
			list2.append(x)
		self.fields['doctors_available'] = forms.ChoiceField(label = 'Doctors Available', required = False,choices=[(a, b) for a, b in list2])
		list3 = [(1, 'Change Doctor'), (2, 'Keep the currently alloted Doctor')]
		self.fields['choice'] = forms.ChoiceField(label = 'Choose', choices=list3, widget=forms.RadioSelect())

class appointment_edit_treated(forms.Form):
	#patient_id = forms.IntegerField(label = 'Patient_id')
	def __init__(self, *args, **kwargs):
		super(appointment_edit_treated, self).__init__(*args, **kwargs)
		self.fields['patient_room_no'] = forms.CharField(label = 'Room no',max_length = 5)

#update this
class patient_edit(forms.Form):
	#patient_id = forms.IntegerField(label = 'Patient_id')
	def __init__(self, *args, **kwargs):
		super(patient_edit, self).__init__(*args, **kwargs)
		list3 = patients.objects.all()
		list4 = []
		for i in list3:
			y = (i.id, i.patient_name)
			list4.append(y)
		self.fields['patient'] = forms.ChoiceField(label = 'Patient', choices = [(a,b) for a,b in list4])
		self.fields['patient_problem'] = forms.CharField(label = 'Problem',max_length = 500)
		self.fields['patient_date_of_admission'] = forms.DateTimeField(label='date of admission', required = False, initial=datetime.today)
		self.fields['patient_room_no'] = forms.CharField(label = 'Room no',max_length = 5, required = False)
		list1 = doctors.objects.filter(doctor_availability = True)
		list2 = []
		#print (list1)
		for i in list1:
			x = (i.id, i.doctor_name)
			list2.append(x)
		self.fields['doctors_available'] = forms.ChoiceField(label = 'Doctors Available',choices=[(a, b) for a, b in list2])

class bill_inf(forms.Form):
	def __init__(self, *args, **kwargs):
		super(bill_inf, self).__init__(*args, **kwargs)
		list1 = appointment.objects.all()
		self.fields['appointment'] = forms.ChoiceField(label='Appointment ID', choices=[(a.id,a.id) for a in list1])

class bill_search(forms.Form):
	def __init__(self, *args, **kwargs):
		super(bill_search, self).__init__(*args, **kwargs)
		list1 = bill.objects.all()
		self.fields['bill'] = forms.ChoiceField(label='Bill ID', choices=[(a.id,a.id) for a in list1])

class patient_edit(forms.Form):
	#patient_id = forms.IntegerField(label = 'Patient_id')
	def __init__(self, *args, **kwargs):
		super(patient_edit, self).__init__(*args, **kwargs)
		self.fields['patient_name'] = forms.CharField(label = 'Patient-name',max_length = 500)
		self.fields['patient_city_name'] = forms.CharField(label='City',max_length=200)
		self.fields['patient_house_no'] = forms.IntegerField(label='House No.')
		self.fields['patient_street_no'] = forms.IntegerField(label='Street No.')
		self.fields['patient_age'] = forms.IntegerField(label='Age')
		self.fields['patient_gender'] = forms.CharField(label = 'Gender',max_length = 1)
		