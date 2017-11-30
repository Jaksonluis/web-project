# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from users.form import RegistroForm
from django.shortcuts import render

# Create your views here.
class RegisterUsers(CreateView):
    model = User
    template_name = 'apps/LoginAlum.html'
    form_class = RegistroForm
    success_url = reverse_lazy('login')