from django import forms
from datetime import datetime
from manageHospital.models import doctors

list1 = doctors.objects.all().filter(doctor_availability = True)
list2 = []
print (list1)
for i in list1:
	x = (i.id, i.doctor_name)
	list2.append(x)

class login(forms.Form):
    user_id = forms.CharField(label='Login id', max_length=20)
    user_pwd = forms.CharField(label='Password', max_length=20)

class pres(forms.Form):
	prescription = forms.CharField(label='Prescription', max_length=500)
	allot_room = forms.BooleanField(label='Allot Room', required = False)

class bill_inf(forms.Form):
	patient_id = forms.IntegerField(label='Bill')

class patient_det(forms.Form):
	patient_name = forms.CharField(label='Patient-name',max_length=200)
	patient_city_name = forms.CharField(label='City',max_length=200)
	patient_house_no = forms.IntegerField(label='House No.')
	patient_street_no = forms.IntegerField(label='Street No.')
	patient_age = forms.IntegerField(label='Age')
	patient_gender = forms.CharField(label = 'Gender',max_length = 1)
	patient_problem = forms.CharField(label = 'Problem',max_length = 500)
	patient_date_of_admission = forms.DateField(label='date of admission', required = False, initial=datetime.today)
	patient_room_no = forms.CharField(label = 'Room no',max_length = 5, required = False)
	doctors_available = forms.ChoiceField(choices=[(a, b) for a, b in list2])