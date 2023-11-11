from django import forms

from .models import booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'
        