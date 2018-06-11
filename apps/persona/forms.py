from __future__ import absolute_import
from django import forms
from apps.persona.models import cliente


class personaForm(forms.ModelForm):

    class Meta:
        model = cliente

        fields = [
            'tipo_cliente',
            'nombre_cliente',
            'tipo_documento',
            'num_documento',
            'direccion',
            'telefono',
            'correo',
            'estatus',
        ]

        labels = {
            'tipo_cliente':'tipo cliente',
            'nombre_cliente':'cliente',
            'tipo_documento': 'Tipo de Doc.',
            'num_documento': 'RIF',
            'direccion':'Direccion',
            'telefono':'Telefono',
            'correo':'Correo',
            'estatus':'estatus',
        }

        widgets = {
            'tipo_cliente': forms.Select(attrs={'class':'form-control'}),
            'nombre_cliente': forms.TextInput(attrs={'class':'form-control','required':'required','placeholder':'cliente','id':'nombre_cliente'}),
            'tipo_documento': forms.Select(attrs={'class':'form-control'}),
            'num_documento': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'estatus': forms.Select(attrs={'class':'form-control'}),
        }