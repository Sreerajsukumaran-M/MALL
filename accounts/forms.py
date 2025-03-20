

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image', 'phone', 'address']  # Shop owners don't use address

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.role == 'shop_owner':
            self.fields.pop('address')  # Remove address field for shop owners
