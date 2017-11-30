from django import forms
from models import Becarios
class RegistroForms(forms.ModelForm):

    class Meta:
        model = Becarios

        fields = [
            'Nocontrol',
			'Nombrealum',
			'Appalum',
			'Apmalum',
			'Caralum',
			'Semalum',
        ]

        labels = {
            'Nocontrol': 'No. Control',
            'Nombrealum': 'Nombre del alumno',
            'Appalum': 'Apellido paterno',
            'Apmalum': 'Apellido materno',
            'Caralum': 'Carrera',
            'Semalum': 'Semestre',
        }


class ChequeoForms(forms.Form):
    nocontrol = forms.IntegerField()
    FecReg = forms.DateTimeField(required=False)



