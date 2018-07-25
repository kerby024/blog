# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = 'Placeholder to later display all the list of users!'
    return HttpResponse(response)

def register(request):
    response = 'Placeholder for users to create a new record!'
    return HttpResponse(response)

def login(request):
    response = 'Placeholder for user to login!'
    return HttpResponse(response)

def new(request):
    return redirect('/users/register')

# Create your views here.
