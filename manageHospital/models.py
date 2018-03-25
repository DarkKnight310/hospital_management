from django.db import models

# Create your models here.

class receptionist(models.Model):
    receptionist_name = models.CharField(max_length=200);
    receptionist_date_of_joining = models.DateTimeField();
    receptionist_salary = models.IntegerField()
    receptionist_login = models.CharField(max_length=20, default='secret')

class patients(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_city_name = models.CharField(max_length=200)
    patient_house_no = models.IntegerField()
    patient_street_no = models.IntegerField()
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length = 200)

class room(models.Model):
    charge = models.IntegerField(default=200)

class appointment(models.Model):
    receptionist_id = models.ForeignKey(receptionist,on_delete=models.CASCADE)
    patient_id = models.ForeignKey(patients,on_delete=models.CASCADE)
    room_id = models.ForeignKey(room, on_delete=models.CASCADE, null=True)
    patient_date_of_admission = models.DateTimeField()
    patient_problem = models.CharField(max_length = 500)
    treated = models.BooleanField(default = False)

class patient_phone_number(models.Model):
    patient_id = models.ForeignKey(patients, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length = 10)

class department(models.Model):
    dep_name = models.CharField(max_length = 50)
    office_no = models.CharField(max_length = 5)

class doctors(models.Model):
    doctor_name = models.CharField(max_length=200)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)
    doctor_s_time = models.TimeField(blank=True)
    doctor_e_time = models.TimeField(blank=True)
    doctor_date_of_joining = models.DateField(blank=True)
    doctor_availability = models.BooleanField(default=True)
    doctor_degree = models.CharField(max_length=10)
    doctor_salary = models.IntegerField()
    doctor_consultation_fee = models.IntegerField()
    doctor_login = models.CharField(max_length=20, default='secret')

class doctor_phone_number(models.Model):
    doctor_id = models.ForeignKey(doctors, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length = 10)

class consults(models.Model):
    appointment_id = models.ForeignKey(appointment, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctors, on_delete=models.CASCADE)
    allot_room = models.BooleanField(default = True)
    prescription = models.CharField(max_length=200)

class belongs_to(models.Model):
    doctor_id = models.ForeignKey(doctors, on_delete=models.CASCADE)
    department_id = models.ForeignKey(department, on_delete=models.CASCADE)


class bill(models.Model):
    appointment_id = models.ForeignKey(appointment, on_delete=models.CASCADE)
    discharge_time = models.DateTimeField()
    amount = models.IntegerField(default=0)

class maintains(models.Model):
    receptionist_id = models.ForeignKey(receptionist,on_delete=models.CASCADE)
    bill_id = models.ForeignKey(bill,on_delete=models.CASCADE)


class login_details(models.Model):
    type = models.CharField(max_length=1)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)



# class Choice(models.Model):
  #  question = models.ForeignKey(Question, on_delete=models.CASCADE)
   # choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)