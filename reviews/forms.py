from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Напишите ваш отзыв...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
