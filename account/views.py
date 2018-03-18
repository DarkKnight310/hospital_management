# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from manageHospital import models
from .forms import login

# Create your views here.

def first_page(request):
	return render_to_response('first_page.html')

def doctorlogin(request):
	user_type = "Doctor"
	return render_to_response('login.html', {'user_type': user_type})

def receptionistlogin(request):
	user_type = "Receptionist"
	return render_to_response('login.html', {'user_type': user_type})

def doctor_home(request):
	return render_to_response('doctor_home.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = login()

    return render_to_response('login_withform.html', {'form': form})