from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'dosage', 'reminder_time', 'repeat_daily']
        widgets = {
            'reminder_time': forms.TimeInput(attrs={'type': 'time'}),
        }
