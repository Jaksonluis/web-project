# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from form import RegistroForms, ChequeoForms
from models import Becarios, Registro
import datetime
# Create your views here.
def base(request):
    return render(request,'apps/Base.html')

def Registro_view(request):
    if request.method == 'POST':
        form = RegistroForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('base_view')
    else:
        form = RegistroForms()

        return render(request, 'apps/Registro.html', {'form': form})


def Chequeo_view(request):
    form = ChequeoForms(request.POST or None)
    mensaje=""
    verificar = False
    verificar2 = False
    alumno = Becarios.objects.all()
    fecha = Registro.objects.all()
    f = Registro.objects.filter(FechaReg=datetime.datetime.now().date())
    print (form.is_valid())
    if form.is_valid():
        print (request.user.is_superuser)
        if request.user.is_superuser:
            nocontrol1 = form.cleaned_data["nocontrol"]
            for alumn in alumno:
                print (nocontrol1 == alumn.Nocontrol)
                if nocontrol1 == alumn.Nocontrol:
                    verificar=True
                    for fec in fecha:
                        if alumn == fec.nocontrol:
                            verificar2=True
                            mensaje="Ya checaste el dia de hoy"
                    if verificar2 == False:
                        p = Registro(nocontrol=alumn,FecReg=datetime.datetime.now(),FechaReg=datetime.datetime.now().date())
                        p.save()
                        mensaje="Comida Registrada"

            if verificar == False:
                mensaje="Alumno no registrado en el sistema"


            form=ChequeoForms()
    return render(request,'apps/Chequeo.html',{"form":form,"Mensaje":mensaje})


#def Mostrar_view(request):
class Becarios_report(ListView):
    template_name = "apps/Becarios_report.html"
    model = Registro

