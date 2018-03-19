from django import forms

class login(forms.Form):
    user_id = forms.CharField(label='Login id', max_length=20)
    user_pwd = forms.CharField(label='Password', max_length=20)

class patient_det(forms.Form):
	patient_name = forms.CharField(label='Patient-name',max_length=200)
	patient_city_name = forms.CharField(label='City',max_length=200)
	patient_house_no = forms.IntegerField(label='House No.')
	patient_street_no = forms.IntegerField(label='Street No.')
	patient_age = forms.IntegerField(label='Age')
	patient_gender = forms.CharField(label = 'Gender',max_length = 1)
	patient_problem = forms.CharField(label = 'Problem',max_length = 500)
	patient_date_of_admission = forms.DateTimeField(label='date of admission', required = False)
	patient_room_no = forms.CharField(label = 'Room no',max_length = 5, required = False)

  