from django import forms
from .models import DoctorProfile


class DoctorProfileForm(forms.ModelForm):

    class Meta:

        model = DoctorProfile

        fields = [
            'qualification',
            'specialization',
            'experience',
            'consultation_fee',
            'hospital_name',
            'address',
            'city',
            'state',
            'bio',
            
        ]

        widgets = {

            'qualification': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'specialization': forms.Select(attrs={
                'class': 'form-select'
            }),

            'experience': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'consultation_fee': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'hospital_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'state': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

           
        }