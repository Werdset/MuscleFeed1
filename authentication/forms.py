from django import forms
from django.core.exceptions import ValidationError
from .models import Profile, EmailVerification

class SignupFormStep1(forms.Form):
    email = forms.EmailField()
    agreed = forms.BooleanField(required=True)

class SignupFormStep3(forms.Form):
    user_name = forms.CharField()
    user_surname = forms.CharField()
    user_sex = forms.ChoiceField(choices=Profile.SEX_CHOICES)
    user_phone = forms.CharField()
    user_address = forms.CharField()

class AccountChangeEmailForm(forms.Form):
    new_email = forms.EmailField()

class AccountChangePersonalDataForm(forms.Form):
    new = forms.CharField()
