from django.core import validators
from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
	class Meta:
		model = UserDetails
		fields = ['username','email','password','address']
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.EmailInput(attrs={'class':'form-control'}),
			'password' : forms.PasswordInput(attrs={'class':'form-control'}),
			'address' : forms.TextInput(attrs={'class':'form-control'}),
		}
