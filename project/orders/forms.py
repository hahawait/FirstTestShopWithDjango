from django import forms
from .models import Order

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'email': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'postal_code': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }