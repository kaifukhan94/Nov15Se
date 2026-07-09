from django import forms
from .models import DoctorAvailability


class DoctorAvailabilityForm(forms.ModelForm):

    class Meta:
        model = DoctorAvailability

        fields = [
            'day',
            'start_time',
            'end_time',
            'is_active'
        ]

        widgets = {

            'day': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'start_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),

            'end_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),

            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }