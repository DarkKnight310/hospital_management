from django.db import models

# Create your models here.

class patients(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_city_name = models.CharField(max_length=200)
    patient_house_no = models.IntegerField();
    patient_street_no = models.IntegerField();
    patient_age = models.IntegerField();
    patient_date_of_admission = models.DateTimeField('date published')
    patient_gender = models.CharField(max_length = 200)
    patient_problem = models.CharField(max_length = 500);
    def __str__(self):
        return self.patient_problem

# class Choice(models.Model):
  #  question = models.ForeignKey(Question, on_delete=models.CASCADE)
   # choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)