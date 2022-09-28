from django import forms
from .models import Entrada, Reporte, PerfilOf

class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['asunto', 'detalle', 'importante']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto: '}),
            'detalle': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Realize el reporte aquí: '}),
            'importante': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto' }),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilOf
        fields = ['nombre', 'telefono', 'ubicacion','puesto','codigo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ': '}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ': '}),
            'puesto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ': '}),
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ': '}),
            'ubicacion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Distrito / Canton / Provincia '}),
        }