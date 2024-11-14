from django import forms
from .models import CallRequest

class CallRequestForm(forms.ModelForm):
    class Meta:
        model = CallRequest
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите ваш телефон'}),
        }
