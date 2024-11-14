from django import forms
from .models import Order, OrderFreeze

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['total_price']

class OrderFreezeForm(forms.ModelForm):
    class Meta:
        model = OrderFreeze
        fields = ['frozen_from', 'frozen_to']
